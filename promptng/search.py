################################################################################
#                                   PromptNG                                   #
#                                                                              #
# Composes, manages, and orchestrates reusable AI prompt components            #
#                                                                              #
# Change History                                                               #
# 04/13/2026  Esteban Herrera Original code.                                   #
#                           Add new history entries as needed.                 #
#                                                                              #
#                                                                              #
################################################################################
################################################################################
################################################################################
#                                                                              #
#  Copyright (c) 2026-present Esteban Herrera C.                               #
#  stv.herrera@gmail.com                                                       #
#                                                                              #
#  This program is free software; you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation; either version 3 of the License, or           #
#  (at your option) any later version.                                         #
#                                                                              #
#  This program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with this program; if not, write to the Free Software                 #
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA   #

# search.py
# A modular CLI search utility that scans a structured prompts/ directory and
# ranks reusable prompt files by relevance using token-based and wildcard
# matching, enabling fast discovery of prompt components by name or content.

import argparse
import json
import os
import re
from pathlib import Path

# Builds an absolute path to a directory named prompts
PROMPTS_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "prompts"
)


def tokenize(text):
    """
    Extracts and normalizes word tokens from a string.

    Converts the input text to lowercase and returns a list of
    alphanumeric word tokens using a regular expression.

    Args:
        text (str): The input string to tokenize.

    Returns:
        List[str]: A list of lowercase word tokens.
    """
    return re.findall(r"\w+", text.lower())


def boost_score(query: str, name: str, category: str) -> float:
    """
    Computes an additional relevance boost based on matches between the query
    and the target's filename and category.

    This function applies heuristic weighting to prioritize results where the
    query closely matches the filename or, to a lesser extent, the category:

    - Filename boosts (highest impact):
        * Exact match with full filename → large boost
        * Token match within filename → strong boost
        * Substring match within filename → moderate boost

    - Category boosts (lower impact):
        * Token match within category → small boost
        * Substring match within category → minimal boost

    The boost is additive and intended to complement the base relevance score,
    helping promote more intuitive and user-expected ranking (e.g., exact
    filename matches appearing first).

    Args:
        query (str): The search query string.
        name (str): The filename (without extension) of the item.
        category (str): The category or top-level folder of the item.

    Returns:
        float: The computed boost score to be added to the base relevance score.
    """
    query_tokens = tokenize(query)
    name_tokens = tokenize(name)
    category_tokens = tokenize(category)

    boost = 0.0

    for q in query_tokens:
        # --- Filename boosts (strong) ---
        if q == name:
            boost += 15.0  # exact filename match
        elif q in name_tokens:
            boost += 8.0   # token match in filename
        elif q in name:
            boost += 4.0   # substring in filename

        # --- Category boosts (weaker) ---
        if q in category_tokens:
            boost += 3.0
        elif q in category:
            boost += 1.5

    return boost


def score_match(query: str, name: str, content: str) -> float:
    """
    Computes a base relevance score between a search query and a target item
    using weighted matching against its filename and content.

    The function supports two modes:

    - Wildcard mode:
        Triggered when the query contains '*'. The query is converted into a
        case-insensitive regular expression where '*' matches any sequence of
        characters. Matches contribute:
            * +3.0 if found in the filename
            * +1.0 if found in the content (first 2000 characters only)

    - Token mode:
        The query, filename, and content are tokenized into lowercase words.
        Each query token is compared against tokens in the filename and content,
        accumulating a score based on match quality:

        Filename matches (higher weight):
            * Exact match       → +3.0
            * Prefix match      → +2.0
            * Substring match   → +1.5

        Content matches (lower weight):
            * Exact match       → +1.0
            * Prefix match      → +0.5
            * Substring match   → +0.25

        Content evaluation is limited to the first 2000 characters for
        performance.

    The resulting score is unbounded and intended for relative ranking only.
    It does not represent a normalized or percentage-based relevance.

    Args:
        query (str): The search query, optionally containing wildcards (*).
        name (str): The filename (without extension) of the item.
        content (str): The textual content associated with the item.

    Returns:
        float: The computed relevance score (higher means more relevant).
    """
    score = 0.0

    # wildcard mode
    if "*" in query:
        pattern = re.compile(
            re.escape(query).replace(r"\*", ".*"),
            re.IGNORECASE
        )

        if pattern.search(name):
            score += 3.0
        if pattern.search(content[:2000]):
            score += 1.0

        return score

    # token mode
    query_tokens = tokenize(query)
    name_tokens = tokenize(name)
    content_tokens = tokenize(content[:2000])

    for q in query_tokens:
        for t in name_tokens:
            if t == q:
                score += 3.0
            elif t.startswith(q):
                score += 2.0
            elif q in t:  # substring match
                score += 1.5

        for t in content_tokens:
            if t == q:
                score += 1.0
            elif t.startswith(q):
                score += 0.5
            elif q in t:  # substring match
                score += 0.25

    return score


def search(query, category=None, limit=10):
    """
    Searches the PromptNG prompts directory for files matching a query and
    returns the top results ranked by relevance.

    The function recursively scans the `PROMPTS_DIR` directory, filtering files
    by supported extensions, and computes a relevance score for each file based on:

    - Base matching score (`score_match`): compares the query against the
      filename and file content (first 2000 characters)
    - Heuristic boosts (`boost_score`): prioritizes matches in the filename
      and category (folder)

    Only results with a positive score are included. Results are sorted in
    descending order of score and limited to the specified number.

    Args:
        query (str): The search query string.
        category (str, optional): If provided, restricts results to a specific
            top-level category (folder).
        limit (int, optional): Maximum number of results to return (default: 10).

    Returns:
        List[dict]: A list of result objects, each containing:
            - "category" (str): Top-level folder name
            - "name" (str): Filename without extension
            - "path" (str): Relative path from PROMPTS_DIR
            - "score" (float): Relevance score

    Notes:
        - Only files with allowed extensions (.md, .yaml, .yml, .json, .txt)
          are considered.
        - File content is safely read; unreadable files are treated as empty.
        - Scores are relative and intended for ranking, not absolute comparison.
    """
    results = []
    query_tokens = tokenize(query)

    ALLOWED_EXTENSIONS = (".md", ".yaml", ".yml", ".json", ".txt")

    for root, _, files in os.walk(PROMPTS_DIR):
        for file in files:
            if not file.endswith(ALLOWED_EXTENSIONS):
                continue

            path = Path(root) / file
            rel_path = path.relative_to(PROMPTS_DIR)

            parts = rel_path.parts
            file_category = parts[0]

            if category and file_category != category:
                continue

            name = path.stem

            try:
                content = path.read_text(encoding="utf-8")
            except Exception:
                content = ""

            score = score_match(query, name, content)

            if score > 0:
                score += boost_score(query, name, file_category)

                results.append({
                    "category": file_category,
                    "name": name,
                    "path": str(rel_path),
                    "score": score
                })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:limit]


def print_human(results):
    """
    Prints search results in a human-readable format.

    Displays a summary of the number of matches followed by each result's
    category, name, score, and relative path. File extensions such as
    `.md` and `.yaml` are removed from the displayed path for readability.

    If no results are provided, a message indicating that no matches were
    found is printed.

    Args:
        results (List[dict]): A list of search result objects, each containing:
            - "category" (str): Top-level folder name
            - "name" (str): Filename without extension
            - "path" (str): Relative file path
            - "score" (float): Relevance score

    Returns:
        None
    """
    if not results:
        print("No matches found.")
        return

    print(f"Found {len(results)} matches:\n")

    for r in results:
        # remove extension (.md / .yaml)
        clean_path = r["path"].replace(".md", "").replace(".yaml", "")

        print(
            f"[{r['category']}] {r['name']}  (score: {round(r['score'], 2)})\n"
            f"  → /{clean_path}"
        )


def main():
    """
    Serves as the entry point for the PromptNG search CLI.

    Parses command-line arguments, executes a search over the prompts
    directory, and outputs the results in either human-readable or JSON format.

    Command-line arguments:
        query (str): The search query string.
        --category (str, optional): Restrict results to a specific category.
        --limit (int, optional): Maximum number of results to return (default: 10).
        --json (flag): If set, outputs results as formatted JSON instead of
            human-readable text.

    Behavior:
        - Invokes the `search` function with the provided parameters.
        - Outputs results using `print_human` by default.
        - If `--json` is specified, prints the raw results as JSON.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Search PromptNG prompts")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--category", help="Filter by category")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--json", action="store_true")

    args = parser.parse_args()

    results = search(args.query, args.category, args.limit)

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print_human(results)


if __name__ == "__main__":
    main()

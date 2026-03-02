#!/bin/bash

BASE_DIR="$(dirname "$0")/prompts"

load_file() {
    cat "$BASE_DIR/$1/$2.md"
}

compose_prompt() {
    ROLE=$(yq '.role' "$AGENT_FILE")
    TASK=$(yq '.task' "$AGENT_FILE")
    PATTERNS=$(yq '.patterns[]' "$AGENT_FILE")

    PROMPT=""

    PROMPT+="$(load_file roles $ROLE)"
    PROMPT+="\n\n"
    PROMPT+="$(load_file tasks $TASK)"
    PROMPT+="\n\n"

    for P in $PATTERNS; do
        PROMPT+="$(load_file patterns $P)"
        PROMPT+="\n\n"
    done

    echo -e "$PROMPT"
}

# Python Integration

PromptPro can be seamlessly integrated into Python workflows for testing, automation, and scripting. Whether you're validating CLI behavior, building test suites, or invoking PromptPro programmatically, Python provides multiple safe and flexible execution patterns.

This section demonstrates recommended approaches for running PromptPro commands using Python’s subprocess module, along with best practices for error handling, portability, and security.

## Full Test File With try/except

```py
import subprocess
import sys


def test_pp_list_roles():
    try:
        result = subprocess.run(
            [sys.executable, "-m", "promptpro.main", "list", "roles"],
            capture_output=True,
            text=True,
            check=True  # raises exception if command fails
        )

        # Validate output
        assert result.stdout.strip() != "", "No output returned"

        print("STDOUT:")
        print(result.stdout)

        print("STDERR:")
        print(result.stderr)

    except subprocess.CalledProcessError as e:
        print("Command failed!")
        print("Return code:", e.returncode)
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)

    except FileNotFoundError as e:
        print("Executable not found:", e)


if __name__ == "__main__":
    test_pp_list_roles()

```

## shell=True Version

```py
import subprocess


def test_pp_list_roles():
    try:
        subprocess.run(
            "pp list roles",
            check=True,
            shell=True
        )

    except subprocess.CalledProcessError as e:
        print(f"Error executing subprocess command: {e}")


if __name__ == "__main__":
    test_pp_list_roles()

```

### shell=True And "String Command"

✔ Good for: tmux, pipes, redirects  
❌ Risky (shell injection)  
❌ Less portable

Recommended style:

```py
["pp", "list", "roles"]
```

✔ Safer  
✔ Cross-platform (Windows/Linux)  
✔ No quoting issues

## Combine Both Patterns Cleanly

```py
import subprocess
import sys


def run_command(cmd):
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout

    except subprocess.CalledProcessError as e:
        print(f"Error executing subprocess command: {e}")
        print("STDERR:", e.stderr)
        return None


if __name__ == "__main__":
    output = run_command([sys.executable, "-m", "promptpro.main", "list", "roles"])
    
    if output:
        print(output)

```

### Takeaway

* Use check=True → lets you handle failures cleanly

* Catch CalledProcessError → for command errors

* Prefer list args over shell=True → unless you really need shell features

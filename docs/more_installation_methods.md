# More Installation Methods

## More uv Options

### Install Specific Python Versions

In the previous installation step, you can specify a Python version after the `install` option:

```bash
uv python install 3.14
```

### PromptPro Uninstallation

```bash
uv tool uninstall promptpro
```

## Installing PromptPro With pip

These methods require pip already installed on your machine or Python environment.

### Local Installation

Using pip or pip3:

```bash
cd prompt-pro
pip3 install .
```

### Install From PyPI

Using pip or pip3:

```bash
pip install promptpro  # or pip3 depending on your system
```

### Example

After installation, you can import PromptPro in your Python scripts.

```py
# test_promptpro.py

from promptpro.main import main

if __name__ == "__main__":
    main()
```

The script will forward CLI arguments to PromptPro.

To run the script:

```bash
python /path/to/test_promptpro.py list agents
```

This command displays a list of existing agents.

## Use Your CLI Anywhere

Once installed, you can call your CLI (pp) as if it were run from the terminal.

### Examples

[Python Integration](../README.md#-python-integration)

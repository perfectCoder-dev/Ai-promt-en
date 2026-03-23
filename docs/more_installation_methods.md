# More Installation Methods

## More uv Options

### Install Specific Python versions

In the installation step #4, you can specify a Python version after the `install` option:

```bash
uv python install 3.14
```

### PromptPro Uninstallation

```bash
uv tool uninstall promptpro
```

## PromptPro Installations With pip

These methods require pip already installed on your machine or Python environment.

### Local Installation

Using pip or pip3:

```bash
cd prompt-pro
pip3 install .
```

### Install From PyPi

Using pip or pip3:

```bash
pip3 install promptpro
```

### Example

After the installation you can import PromptPro in a script.

```py
# test_promptpro.py

from promptpro.main import main

if __name__ == "__main__":
    main()
```

To run the script:

```bash
python /path/to/test_promptpro.py list agents
```

The command will display a list of existing agents.

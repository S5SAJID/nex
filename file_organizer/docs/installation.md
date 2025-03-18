# nex Installation Guide

This guide provides detailed instructions for installing nex on different operating systems.

## Prerequisites

- Python 3.7 or later
- pip (Python package manager)
- Git (for installation from GitHub)

## Current Installation Method

Currently, nex is only available for installation from GitHub:

### Installing from GitHub

```bash
# Install the latest version from the main branch
pip install git+https://github.com/S5SAJID/nex.git 

# Or, to install a specific version/branch
pip install git+https://github.com/S5SAJID/nex.git@v0.1.0
```

For a user-specific installation (no admin rights):

```bash
pip install --user git+https://github.com/S5SAJID/nex.git
```

### Development Installation

If you want to contribute or modify the code:

```bash
git clone https://github.com/S5SAJID/nex.git
cd nex
pip install -e .
```

## Future Installation Methods

In the future, nex will be available on PyPI and can be installed with:

```bash
pip install nex  # Coming soon
```

## Platform-Specific Notes

### Windows

Make sure Python and Git are added to your PATH during installation. After installing nex, you can run it from the command prompt or PowerShell:

```
nex
```

If you installed with `--user`, the executable might be in:
```
%APPDATA%\Python\Python3x\Scripts\nex
```

### macOS

If you installed Python using Homebrew, you can install nex with:

```bash
pip3 install nex
```

### Linux

Most Linux distributions come with Python pre-installed. You may need to install pip first:

```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install python3-pip

# Fedora
sudo dnf install python3-pip

# Then install nex
pip3 install nex
```

## Verifying Installation

To verify that nex installed correctly:

```bash
nex --help
```

This should display the help message with available options.

## Upgrading

To upgrade to the latest version:

```bash
pip install --upgrade nex
```

## Troubleshooting

### Command Not Found

If you get a "command not found" error:

1. Make sure the Python scripts directory is in your PATH
2. Try installing with:
   ```bash
   pip install --user nex
   ```
   and then add `~/.local/bin` (Linux/macOS) or `%APPDATA%\Python\Python3x\Scripts` (Windows) to your PATH

### Dependency Conflicts

If you encounter dependency conflicts:

1. Consider using a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install nex
   ```

### Permission Errors

If you get permission errors during installation:

1. Try installing with `--user`:
   ```bash
   pip install --user nex
   ```
2. On Unix-like systems, you may need to use sudo (not recommended):
   ```bash
   sudo pip install nex
   ``` 
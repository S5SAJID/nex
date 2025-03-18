# File Organizer Installation Guide

This guide provides detailed instructions for installing File Organizer on different operating systems.

## Prerequisites

- Python 3.7 or later
- pip (Python package manager)

## Installation Methods

### From PyPI (Recommended)

The simplest way to install File Organizer is through pip:

```bash
pip install file-organizer
```

For a user-specific installation (no admin rights):

```bash
pip install --user file-organizer
```

### From Source

If you want the latest development version:

```bash
git clone https://github.com/yourusername/file-organizer.git
cd file-organizer
pip install -e .
```

## Platform-Specific Notes

### Windows

Make sure Python is added to your PATH during installation. After installing, you can run File Organizer from the command prompt or PowerShell:

```
file-organizer
```

If you installed with `--user`, the executable might be in:
```
%APPDATA%\Python\Python3x\Scripts\file-organizer
```

### macOS

If you installed Python using Homebrew, you can install File Organizer with:

```bash
pip3 install file-organizer
```

### Linux

Most Linux distributions come with Python pre-installed. You may need to install pip first:

```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install python3-pip

# Fedora
sudo dnf install python3-pip

# Then install File Organizer
pip3 install file-organizer
```

## Verifying Installation

To verify that File Organizer installed correctly:

```bash
file-organizer --help
```

This should display the help message with available options.

## Upgrading

To upgrade to the latest version:

```bash
pip install --upgrade file-organizer
```

## Troubleshooting

### Command Not Found

If you get a "command not found" error:

1. Make sure the Python scripts directory is in your PATH
2. Try installing with:
   ```bash
   pip install --user file-organizer
   ```
   and then add `~/.local/bin` (Linux/macOS) or `%APPDATA%\Python\Python3x\Scripts` (Windows) to your PATH

### Dependency Conflicts

If you encounter dependency conflicts:

1. Consider using a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install file-organizer
   ```

### Permission Errors

If you get permission errors during installation:

1. Try installing with `--user`:
   ```bash
   pip install --user file-organizer
   ```
2. On Unix-like systems, you may need to use sudo (not recommended):
   ```bash
   sudo pip install file-organizer
   ``` 
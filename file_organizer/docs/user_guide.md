# nex User Guide

## Introduction

nex is a powerful CLI tool that helps you clean up messy directories by automatically organizing files into categorized folders based on their file types. It provides a rich, interactive interface that guides you through the organization process and ensures you maintain control over what happens to your files.

## Installation

```bash
# Install from GitHub
pip install git+https://github.com/S5SAJID/nex.git

# Verify installation
nex --help
```

## Basic Usage

The simplest way to use nex is to run it without any arguments:

```bash
nex
```

This will start the interactive CLI guide that will:
1. Ask you which directory to organize
2. Scan the directory and show you what files will be moved
3. Let you confirm which categories you want to organize
4. Check for duplicate files and let you handle them
5. Process the files and provide a summary

## Command Line Options

For more advanced usage, nex supports several command-line arguments:

```bash
# Organize a specific directory
nex --dir /path/to/directory

# Exclude specific file patterns
nex --exclude "*.log" --exclude "temp/*"

# Skip project structure detection
nex --no-project-detection
```

## Project Structure Detection

When nex detects that it's running in a project directory (containing files like `requirements.txt`, `package.json`, or directories like `src`, `.git`, etc.), it takes extra precautions:

1. It identifies critical project files that shouldn't be moved
2. It shows a warning that you're organizing a project directory
3. It displays a list of excluded files
4. It asks for explicit confirmation before proceeding

This feature helps prevent breaking functional project structures by accidentally moving important files.

## Categories

nex sorts files into the following categories:

| Category     | Extensions                                     |
|--------------|------------------------------------------------|
| Audio        | mp3, wav, flac, m4a, aac, ogg                  |
| Videos       | mp4, avi, mkv, mov, wmv, flv                   |
| Images       | jpg, jpeg, png, gif, bmp, tiff, webp           |
| Documents    | pdf, doc, docx, xls, xlsx, ppt, pptx, txt, rtf |
| Archives     | zip, rar, 7z, tar, gz                          |
| Programming  | py, js, html, css, java, c, cpp, php, etc.     |
| Executables  | exe, msi, app, dmg                             |
| Fonts        | ttf, otf, woff, woff2                          |
| E-books      | epub, mobi, azw, azw3, fb2                     |
| Design       | psd, ai, svg, sketch, xd, fig                  |
| Misc         | All other file types                           |

## Handling Duplicates

nex can detect duplicate files by comparing their content (not just filenames). When duplicates are found:

1. Files are grouped by identical content
2. The first file in each group is marked to keep (default)
3. You can confirm which duplicates to remove
4. Removal requires explicit confirmation

This feature helps reclaim disk space while ensuring you don't lose unique files.

## Troubleshooting

### Permission Errors

If you see "Permission denied" errors:
- Make sure you have read/write access to the directory you're organizing
- Try running the tool with elevated permissions (if appropriate for your environment)

### Project Files Being Moved

If important project files are being moved when they shouldn't be:
- Use the `--exclude` option to specify patterns to exclude
- If a project isn't being detected correctly, create an issue on our GitHub repository

### Program Hangs on Large Files

When processing very large files:
- nex reads files in chunks to calculate hashes
- This might take some time for extremely large files
- Consider excluding very large files with `--exclude` if this is a problem 
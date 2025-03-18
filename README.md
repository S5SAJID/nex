# File Organizer

An interactive CLI tool to organize messy directories by categorizing files into appropriate folders.

## Features

- Scans directories for files and categorizes them by extension
- Moves files to appropriate category folders (Videos, Images, Documents, etc.)
- Detects and handles duplicate files
- Interactive CLI with rich colorful interface
- User confirmation for all operations

## Installation
```bash
pip install file-organizer
```

## Usage
Run the tool:
```bash
file-organizer
```

## Follow the interactive prompts to:
1. Select a directory to organize
2. Review and confirm file categorization
3. Identify and handle duplicate files
4. Complete the organization process

## Categories

Files are organized into the following categories based on their extensions:

- Audio (mp3, wav, flac, etc.)
- Videos (mp4, avi, mkv, etc.)
- Images (jpg, png, gif, etc.)
- Documents (pdf, doc, txt, etc.)
- Archives (zip, rar, 7z, etc.) 
- Programming (py, js, html, etc.)
- Misc (all other files)

## Project Structure Detection

File Organizer automatically detects when it's running in a project directory (containing files like `requirements.txt`, `package.json`, or directories like `src`, `.git`, etc.) and takes special care:

- Critical project files like `main.py`, `README.md`, and configuration files won't be moved
- A warning will be shown before organizing project directories
- You'll get a chance to review excluded files before proceeding

### Command Line Options

```
file-organizer --dir /path/to/directory  # Specify directory to organize
file-organizer --exclude "*.py"          # Exclude Python files
file-organizer --exclude "data/*"        # Exclude files in data directory
file-organizer --no-project-detection    # Disable project detection
```

## Limitations

While File Organizer tries to be smart about detecting project structures, it's not perfect. Always review the proposed changes before confirming, especially in development directories.

## License
MIT

## Documentation

For detailed documentation, see the [docs directory](file_organizer/docs/index.md):

- [User Guide](file_organizer/docs/user_guide.md)
- [API Documentation](file_organizer/docs/api_docs.md)
- [Examples](file_organizer/docs/examples.md)
- [Contributing](file_organizer/docs/contributing.md)
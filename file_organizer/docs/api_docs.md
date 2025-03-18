# File Organizer API Documentation

This document describes the internal API of File Organizer for developers who want to use it programmatically or extend its functionality.

## Core Classes

### FileOrganizer

The `FileOrganizer` class in `file_organizer/organizer.py` handles the core organization logic.

```python
from file_organizer.organizer import FileOrganizer

# Initialize with a directory and optional exclusions
organizer = FileOrganizer("/path/to/directory", exclusions=["*.log", "temp/*"])

# Check if this is a project directory
is_project = organizer.detect_project_structure()

# Identify project files that shouldn't be moved
project_files = organizer.identify_project_files()

# Scan the directory and categorize files
file_map = organizer.scan_directory()

# Find duplicate files
duplicates = organizer.find_duplicates()

# Organize files in a category
moves = organizer.organize_files("Images", files_to_move)

# Execute the moves
successful_moves = organizer.execute_move(moves)

# Remove duplicate files
removed_files = organizer.remove_duplicates(files_to_remove)

# Get statistics about the organization
stats = organizer.get_stats()
```

#### Methods

| Method | Description |
|--------|-------------|
| `__init__(source_dir, exclusions=None)` | Initialize with source directory and optional exclusion patterns |
| `detect_project_structure()` | Check if this appears to be a project directory |
| `identify_project_files()` | Find critical project files that shouldn't be moved |
| `should_exclude(file_path)` | Check if a file should be excluded |
| `scan_directory()` | Scan and categorize files in the directory |
| `get_file_hash(file_path)` | Calculate SHA-256 hash of a file |
| `find_duplicates()` | Find duplicate files based on content hash |
| `organize_files(category, files_to_move)` | Set up file moves for a category |
| `remove_duplicates(duplicates_to_remove)` | Remove duplicate files |
| `execute_move(moves)` | Execute file moves |
| `get_stats()` | Get statistics about the organization process |

### FileOrganizerCLI

The `FileOrganizerCLI` class in `file_organizer/cli.py` provides an interactive CLI interface using Rich.

```python
from file_organizer.cli import FileOrganizerCLI

# Initialize the CLI
cli = FileOrganizerCLI()

# Run the interactive CLI
cli.run()
```

#### Methods

| Method | Description |
|--------|-------------|
| `__init__()` | Initialize the CLI interface |
| `select_directory()` | Prompt user to select a directory |
| `display_file_map(file_map)` | Display categorized files |
| `confirm_organization(file_map)` | Ask for confirmation to organize |
| `display_duplicates(duplicate_groups)` | Display duplicates and get confirmation |
| `run()` | Run the full CLI workflow |

## Utilities

### Categories

The `categories.py` module defines file extension categories.

```python
from file_organizer.categories import get_category, CATEGORIES

# Get category for a file extension
category = get_category("pdf")  # Returns "Documents"

# Access the category mapping directly
all_categories = CATEGORIES
```

### Example: Custom File Processing

Here's how you could extend File Organizer for custom file processing:

```python
from file_organizer.organizer import FileOrganizer
from pathlib import Path

class CustomFileOrganizer(FileOrganizer):
    def __init__(self, source_dir, exclusions=None, custom_categories=None):
        super().__init__(source_dir, exclusions)
        self.custom_categories = custom_categories or {}
        
    def get_custom_category(self, file_path):
        """Apply custom categorization rules based on content or naming patterns"""
        # Example: Categorize by file size
        file_size = file_path.stat().st_size
        if file_size > 100 * 1024 * 1024:  # > 100MB
            return "Large Files"
        
        # Fall back to extension-based categorization
        return super().get_category(file_path.suffix.lstrip('.'))
        
    def scan_directory(self):
        """Override to use custom categorization"""
        # Your custom implementation
        # ...
``` 
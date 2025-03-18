# File Organizer Examples

This document provides practical examples of how to use File Organizer for various scenarios.

## Basic Examples

### Clean up a Downloads Folder

```bash
file-organizer --dir ~/Downloads
```

This will scan your Downloads folder, categorize files, and guide you through organizing them.

### Clean up but Exclude Some Files

```bash
file-organizer --dir ~/Desktop --exclude "*.iso" --exclude "backup*"
```

This will organize your Desktop but leave any ISO files and files starting with "backup" in place.

## Advanced Examples

### Script to Clean Multiple Directories

You can create a shell script to clean multiple directories:

```bash
#!/bin/bash
# clean_directories.sh

directories=(
  "~/Downloads"
  "~/Desktop"
  "~/Documents/temp"
)

for dir in "${directories[@]}"; do
  echo "Cleaning $dir..."
  file-organizer --dir "$dir" --exclude "*.tmp"
done

echo "All directories cleaned!"
```

### Integration with Cron for Scheduled Cleaning

You can schedule File Organizer to run periodically using cron:

```
# Run File Organizer on Downloads folder every Sunday at 1 AM
0 1 * * 0 /usr/local/bin/file-organizer --dir /home/user/Downloads --exclude "*.partial"
```

### Python Script for Custom Processing

You can use File Organizer programmatically in your Python scripts:

```python
import sys
from pathlib import Path
from file_organizer.organizer import FileOrganizer
from file_organizer.cli import FileOrganizerCLI

def cleanup_user_directories(username):
    """Clean up directories for a specific user"""
    user_home = Path(f"/home/{username}")
    
    # Directories to clean
    directories = [
        user_home / "Downloads",
        user_home / "Desktop",
        user_home / "Documents" / "temp"
    ]
    
    # Exclusion patterns
    exclusions = ["*.tmp", "*.partial", "important*"]
    
    for directory in directories:
        if directory.exists() and directory.is_dir():
            print(f"Cleaning {directory}...")
            
            # Initialize the organizer
            organizer = FileOrganizer(str(directory), exclusions=exclusions)
            
            # Check if we should proceed based on project detection
            if organizer.detect_project_structure():
                print(f"Warning: {directory} appears to be a project directory. Skipping.")
                continue
                
            # Scan directory
            file_map = organizer.scan_directory()
            
            # Find duplicates
            duplicates = organizer.find_duplicates()
            
            # Process each category
            for category, files in file_map.items():
                print(f"  Processing {len(files)} files in category {category}")
                moves = organizer.organize_files(category, files)
                successful = organizer.execute_move(moves)
                print(f"  Moved {len(successful)} files to {category}")
                
            # Show statistics
            stats = organizer.get_stats()
            print(f"  Total files processed: {stats['total_files']}")
            print(f"  Categories: {stats['categories']}")
            
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cleanup_script.py <username>")
        sys.exit(1)
        
    cleanup_user_directories(sys.argv[1]) 
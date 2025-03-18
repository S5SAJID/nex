"""
Core functionality for organizing files and handling duplicates.
"""

import os
import shutil
import hashlib
from pathlib import Path

from file_organizer.categories import get_category

class FileOrganizer:
    def __init__(self, source_dir, exclusions=None):
        """
        Initialize the FileOrganizer.
        
        Args:
            source_dir (str): Directory to organize
            exclusions (list): Patterns to exclude from organization
        """
        self.source_dir = Path(source_dir)
        self.file_map = {}  # Maps categories to files
        self.duplicates = []  # List of duplicate files found
        self.is_project_dir = False  # Flag for project directories
        self.project_files = set()  # Project-related files to not move
        self.exclusions = exclusions or []  # Exclusion patterns
        
    def detect_project_structure(self):
        """
        Detect if the directory appears to be a project directory.
        
        Returns:
            bool: Whether this appears to be a project directory
        """
        # Project indicator files
        project_indicators = [
            "requirements.txt",    # Python
            "pyproject.toml",      # Python
            "setup.py",            # Python
            "package.json",        # Node.js
            "Cargo.toml",          # Rust
            "Gemfile",             # Ruby
            "pom.xml",             # Java/Maven
            "build.gradle",        # Java/Gradle
            "CMakeLists.txt",      # C/C++
            "Makefile",            # General
            ".git",                # Git repository
            ".gitignore",          # Git repository
            "docker-compose.yml",  # Docker
            "Dockerfile",          # Docker
        ]
        
        # Check for common project structures
        for indicator in project_indicators:
            if (self.source_dir / indicator).exists():
                self.is_project_dir = True
                return True
                
        # Check for common project directories
        project_dirs = [".git", "src", "tests", "docs", "build", "dist"]
        project_dir_count = sum(1 for d in project_dirs if (self.source_dir / d).is_dir())
        
        if project_dir_count >= 2:  # If 2+ project directories exist
            self.is_project_dir = True
            return True
            
        return False
    
    def identify_project_files(self):
        """
        Identify files that are likely part of a project and shouldn't be moved.
        
        Returns:
            set: Set of files that should not be moved
        """
        if not self.is_project_dir:
            return set()
            
        # Files that should never be moved in a project
        critical_files = {
            "main.py", "app.py", "index.js", "app.js", "main.js",
            "main.go", "main.rs", "Main.java", "README.md", "LICENSE",
            "config.json", "settings.json", ".env", "manage.py",
        }
        
        # Files in the root directory that match critical patterns
        for item in self.source_dir.glob("*"):
            if item.is_file():
                if item.name in critical_files:
                    self.project_files.add(item)
                # Executable scripts should stay in place
                elif item.suffix == ".py" and item.stat().st_mode & 0o100:  # Is executable
                    self.project_files.add(item)
                # Config files generally should stay in place
                elif item.name.startswith(".") or "config" in item.name.lower():
                    self.project_files.add(item)
                    
        return self.project_files
        
    def should_exclude(self, file_path):
        """
        Check if a file should be excluded based on exclusion patterns.
        
        Args:
            file_path (Path): File path to check
            
        Returns:
            bool: Whether the file should be excluded
        """
        # Project files are always excluded
        if file_path in self.project_files:
            return True
            
        # Check custom exclusion patterns
        for pattern in self.exclusions:
            if file_path.match(pattern):
                return True
                
        return False
        
    def scan_directory(self):
        """
        Scan the source directory and categorize files.
        
        Returns:
            dict: Mapping of categories to file lists
        """
        self.file_map = {}
        
        # First check if this is a project directory
        self.detect_project_structure()
        if self.is_project_dir:
            self.identify_project_files()
        
        # Skip these directories when organizing
        skip_dirs = {"Videos", "Audio", "Images", "Documents", 
                    "Archives", "Programming", "Misc", "Executables", 
                    "Fonts", "E-books", "Design"}
        
        try:
            for item in self.source_dir.iterdir():
                # Skip directories and hidden files
                if item.is_dir() and item.name in skip_dirs:
                    continue
                if item.is_file() and not item.name.startswith('.'):
                    try:
                        # Skip excluded files
                        if self.should_exclude(item):
                            continue
                            
                        ext = item.suffix.lstrip('.')
                        category = get_category(ext)
                        
                        if category not in self.file_map:
                            self.file_map[category] = []
                            
                        self.file_map[category].append(item)
                    except Exception as e:
                        print(f"Error processing file {item}: {e}")
        except PermissionError:
            print(f"Permission denied when accessing {self.source_dir}")
            
        return self.file_map
    
    def get_file_hash(self, file_path):
        """
        Calculate SHA-256 hash of a file.
        
        Args:
            file_path (Path): Path to the file
            
        Returns:
            str: Hex digest of file hash
        """
        h = hashlib.sha256()
        
        # Read file in chunks to handle large files
        with open(file_path, 'rb') as f:
            chunk = f.read(65536)  # 64kb chunks
            while chunk:
                h.update(chunk)
                chunk = f.read(65536)
                
        return h.hexdigest()
    
    def find_duplicates(self):
        """
        Find duplicate files based on content hash.
        
        Returns:
            list: Groups of duplicate files
        """
        self.duplicates = []
        hash_map = {}
        
        # Scan all files in all categories
        for category, files in self.file_map.items():
            for file_path in files:
                file_hash = self.get_file_hash(file_path)
                
                if file_hash in hash_map:
                    hash_map[file_hash].append(file_path)
                else:
                    hash_map[file_hash] = [file_path]
        
        # Extract duplicates (files with the same hash)
        for file_hash, files in hash_map.items():
            if len(files) > 1:
                self.duplicates.append(files)
                
        return self.duplicates
    
    def organize_files(self, category, files_to_move):
        """
        Move files to their category folder.
        
        Args:
            category (str): Category name
            files_to_move (list): List of Path objects to move
            
        Returns:
            list: List of (source, destination) paths
        """
        category_dir = self.source_dir / category
        moved_files = []
        
        # Create category directory if it doesn't exist
        if not category_dir.exists():
            category_dir.mkdir()
            
        # Move files to category directory
        for file_path in files_to_move:
            dest_path = category_dir / file_path.name
            
            # Track the move operation
            moved_files.append((file_path, dest_path))
            
        return moved_files
    
    def remove_duplicates(self, duplicates_to_remove):
        """
        Remove duplicate files.
        
        Args:
            duplicates_to_remove (list): List of Path objects to remove
            
        Returns:
            list: List of removed files
        """
        removed_files = []
        
        for file_path in duplicates_to_remove:
            try:
                file_path.unlink()  # Delete the file
                removed_files.append(file_path)
            except Exception as e:
                print(f"Error removing {file_path}: {e}")
                
        return removed_files
    
    def execute_move(self, moves):
        """
        Execute file moves from source to destination.
        
        Args:
            moves (list): List of (source, destination) tuples
            
        Returns:
            list: Successfully moved files
        """
        successful_moves = []
        
        for src, dst in moves:
            try:
                # Handle case where destination already exists
                if dst.exists():
                    # Add a counter to the filename
                    counter = 1
                    while True:
                        new_name = f"{dst.stem}_{counter}{dst.suffix}"
                        new_dst = dst.parent / new_name
                        if not new_dst.exists():
                            dst = new_dst
                            break
                        counter += 1
                
                # Move the file
                shutil.move(str(src), str(dst))
                successful_moves.append((src, dst))
            except Exception as e:
                print(f"Error moving {src} to {dst}: {e}")
                
        return successful_moves
    
    def get_stats(self):
        """
        Get statistics about the organization process.
        
        Returns:
            dict: Statistics including total files, categories, etc.
        """
        total_files = sum(len(files) for files in self.file_map.values())
        return {
            "total_files": total_files,
            "categories": len(self.file_map),
            "duplicate_groups": len(self.duplicates),
            "duplicate_files": sum(len(group) - 1 for group in self.duplicates)
        } 
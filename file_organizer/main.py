"""
Entry point for the nex CLI.
"""

import argparse
import sys
from pathlib import Path
from file_organizer.cli import FileOrganizerCLI
from file_organizer.organizer import FileOrganizer

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Organize files into appropriate folders.")
    parser.add_argument("--dir", "-d", type=str, help="Directory to organize")
    parser.add_argument("--exclude", "-e", action="append", help="Patterns to exclude (can be used multiple times)")
    parser.add_argument("--no-project-detection", action="store_true", help="Disable project detection")
    return parser.parse_args()

def main():
    """Run the file organizer CLI."""
    args = parse_args()
    cli = FileOrganizerCLI()
    
    # If directory is specified, use it
    if args.dir:
        path = Path(args.dir)
        if not path.exists() or not path.is_dir():
            print(f"Error: {args.dir} is not a valid directory")
            sys.exit(1)
            
        # Create organizer with exclusions
        cli.organizer = FileOrganizer(args.dir, exclusions=args.exclude)
        
        # Disable project detection if requested
        if args.no_project_detection:
            cli.organizer.is_project_dir = False
            cli.organizer.project_files = set()
            
        # Run with provided directory
        cli.run()
    else:
        # Run the interactive flow
        cli.run()

if __name__ == "__main__":
    main() 
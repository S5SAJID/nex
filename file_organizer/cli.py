"""
Interactive CLI interface using Rich.
"""

import os
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.tree import Tree

from file_organizer.organizer import FileOrganizer

console = Console()

class FileOrganizerCLI:
    def __init__(self):
        """Initialize the CLI interface."""
        self.console = Console()
        self.organizer = None
    
    def select_directory(self):
        """
        Prompt user to select a directory to organize.
        
        Returns:
            str: Selected directory path
        """
        self.console.print(Panel.fit(
            "[bold blue]File Organizer[/bold blue]\n"
            "This tool will help you organize messy directories by moving files to appropriate folders.",
            title="Welcome",
            border_style="green"
        ))
        
        default_dir = os.getcwd()
        dir_path = Prompt.ask(
            "Enter directory path to organize", 
            default=default_dir
        )
        
        # Validate directory
        path = Path(dir_path)
        if not path.exists() or not path.is_dir():
            self.console.print(f"[bold red]Error:[/bold red] {dir_path} is not a valid directory")
            return self.select_directory()
            
        return dir_path
    
    def display_file_map(self, file_map):
        """
        Display categorized files in a tree structure.
        
        Args:
            file_map (dict): Mapping of categories to file lists
        """
        if not file_map:
            self.console.print("[yellow]No files found to organize.[/yellow]")
            return
            
        self.console.print("\n[bold]Files to organize:[/bold]")
        
        # Create tree for visualization
        tree = Tree("[bold]Categories[/bold]")
        
        for category, files in file_map.items():
            if not files:
                continue
                
            category_node = tree.add(f"[blue]{category}[/blue] ({len(files)} files)")
            
            # Add first 5 files as examples
            for i, file_path in enumerate(files[:5]):
                category_node.add(f"[green]{file_path.name}[/green]")
                
            # Show ellipsis if more files exist
            if len(files) > 5:
                category_node.add(f"[dim]... and {len(files) - 5} more files[/dim]")
                
        self.console.print(tree)
    
    def confirm_organization(self, file_map):
        """
        Ask for user confirmation to organize files.
        
        Args:
            file_map (dict): Mapping of categories to file lists
            
        Returns:
            dict: Categories confirmed for organization
        """
        confirmed_categories = {}
        
        if not file_map:
            return confirmed_categories
            
        for category, files in file_map.items():
            if not files:
                continue
                
            if Confirm.ask(f"Organize {len(files)} files into [blue]{category}[/blue] folder?"):
                confirmed_categories[category] = files
                
        return confirmed_categories
    
    def display_duplicates(self, duplicate_groups):
        """
        Display duplicate files and ask for confirmation to remove.
        
        Args:
            duplicate_groups (list): Groups of duplicate files
            
        Returns:
            list: Files to remove
        """
        if not duplicate_groups:
            self.console.print("[green]No duplicate files found.[/green]")
            return []
            
        files_to_remove = []
        
        self.console.print("\n[bold yellow]Duplicate files found:[/bold yellow]")
        
        for i, group in enumerate(duplicate_groups, 1):
            table = Table(title=f"Duplicate Group {i}")
            table.add_column("Keep?", style="green")
            table.add_column("File Path", style="blue")
            table.add_column("Size", style="cyan")
            
            # Mark first file as "keep" by default
            for j, file_path in enumerate(group):
                keep = "[green]✓[/green]" if j == 0 else "[red]✗[/red]"
                size = f"{file_path.stat().st_size / 1024:.2f} KB"
                table.add_row(keep, str(file_path), size)
                
                # Add all except first to removal list
                if j > 0:
                    files_to_remove.append(file_path)
                    
            self.console.print(table)
        
        if files_to_remove:
            if not Confirm.ask(f"Remove {len(files_to_remove)} duplicate files?"):
                return []
                
        return files_to_remove
    
    def run(self):
        """
        Run the file organizer CLI.
        """
        try:
            # Step 1: Select directory
            dir_path = self.select_directory()
            self.organizer = FileOrganizer(dir_path)
            
            # Check if this is a project directory before scanning
            if self.organizer.detect_project_structure():
                self.console.print(
                    "[bold yellow]Warning:[/bold yellow] This appears to be a project directory. "
                    "Some files will be excluded from organization to preserve functionality."
                )
                project_files = self.organizer.identify_project_files()
                if project_files:
                    self.console.print("[yellow]The following files will be excluded:[/yellow]")
                    for file in project_files:
                        self.console.print(f"  - [blue]{file.name}[/blue]")
                
                proceed = Confirm.ask(
                    "Do you want to proceed with organizing this directory?",
                    default=False
                )
                
                if not proceed:
                    self.console.print("[yellow]Operation cancelled.[/yellow]")
                    return
            
            # Step 2: Scan directory
            with Progress(
                SpinnerColumn(),
                TextColumn("[bold blue]Scanning directory...[/bold blue]"),
                transient=True
            ) as progress:
                progress.add_task("scan", total=None)
                file_map = self.organizer.scan_directory()
                
            # Step 3: Display and confirm file organization
            self.display_file_map(file_map)
            
            if not file_map:
                self.console.print("[yellow]No files found to organize. Exiting.[/yellow]")
                return
                
            confirmed_categories = self.confirm_organization(file_map)
            
            if not confirmed_categories:
                self.console.print("[yellow]No categories selected for organization. Exiting.[/yellow]")
                return
            
            # Step 4: Check for duplicates
            with Progress(
                SpinnerColumn(),
                TextColumn("[bold blue]Checking for duplicates...[/bold blue]"),
                transient=True
            ) as progress:
                progress.add_task("duplicates", total=None)
                duplicate_groups = self.organizer.find_duplicates()
                
            # Step 5: Handle duplicates
            files_to_remove = self.display_duplicates(duplicate_groups)
            
            if files_to_remove:
                with Progress(
                    SpinnerColumn(),
                    TextColumn("[bold red]Removing duplicates...[/bold red]"),
                    transient=True
                ) as progress:
                    progress.add_task("remove", total=None)
                    removed = self.organizer.remove_duplicates(files_to_remove)
                    
                self.console.print(f"[green]Successfully removed {len(removed)} duplicate files.[/green]")
            
            # Step 6: Organize files
            with Progress(
                SpinnerColumn(),
                TextColumn("[bold blue]Organizing files...[/bold blue]"),
                transient=True
            ) as progress:
                progress.add_task("organize", total=None)
                
                for category, files in confirmed_categories.items():
                    moves = self.organizer.organize_files(category, files)
                    successful = self.organizer.execute_move(moves)
                    
                    self.console.print(f"[green]Moved {len(successful)} files to {category} folder.[/green]")
            
            # Final message with statistics
            stats = self.organizer.get_stats()
            self.console.print(Panel.fit(
                f"[bold green]Organization complete![/bold green]\n\n"
                f"Total files processed: {stats['total_files']}\n"
                f"Categories: {stats['categories']}\n"
                f"Duplicate groups found: {stats['duplicate_groups']}\n"
                f"Duplicate files removed: {stats['duplicate_files']}",
                border_style="green",
                title="Summary"
            ))
            
        except KeyboardInterrupt:
            self.console.print("\n[yellow]Operation cancelled by user.[/yellow]")
        except Exception as e:
            self.console.print(f"[bold red]An error occurred:[/bold red] {str(e)}") 
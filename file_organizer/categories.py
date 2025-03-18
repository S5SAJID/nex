"""
Define file extension categories for organizing files.
"""

# Mapping of file extensions to folder names
CATEGORIES = {
    # Audio files
    "mp3": "Audio",
    "wav": "Audio",
    "flac": "Audio",
    "m4a": "Audio",
    "aac": "Audio",
    "ogg": "Audio",
    
    # Video files
    "mp4": "Videos",
    "avi": "Videos",
    "mkv": "Videos",
    "mov": "Videos",
    "wmv": "Videos",
    "webm": "Videos",
    "m4v": "Videos",
    "flv": "Videos",
    
    # Image files
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "gif": "Images",
    "bmp": "Images",
    "tiff": "Images",
    "webp": "Images",
    
    # Documents
    "pdf": "Documents",
    "doc": "Documents",
    "docx": "Documents",
    "xls": "Documents",
    "xlsx": "Documents",
    "ppt": "Documents",
    "pptx": "Documents",
    "txt": "Documents",
    "rtf": "Documents",
    "odt": "Documents",
    
    # Archives
    "zip": "Archives",
    "rar": "Archives",
    "7z": "Archives",
    "tar": "Archives",
    "gz": "Archives",
    
    # Programming
    "py": "Programming",
    "js": "Programming",
    "html": "Programming",
    "css": "Programming",
    "java": "Programming",
    "c": "Programming",
    "cpp": "Programming",
    "php": "Programming",
    "rb": "Programming",
    "go": "Programming",
    "rs": "Programming",
    "ts": "Programming",
    "json": "Programming",
    "xml": "Programming",
    
    # Executable files
    "exe": "Executables",
    "msi": "Executables",
    "app": "Executables",
    "dmg": "Executables",
    
    # Fonts
    "ttf": "Fonts",
    "otf": "Fonts",
    "woff": "Fonts",
    "woff2": "Fonts",
    
    # E-books
    "epub": "E-books",
    "mobi": "E-books",
    "azw": "E-books",
    "azw3": "E-books",
    "fb2": "E-books",
    
    # Design files
    "psd": "Design",
    "ai": "Design",
    "svg": "Design",
    "sketch": "Design",
    "xd": "Design",
    "fig": "Design",
}

def get_category(extension):
    """
    Get the category for a file extension.
    
    Args:
        extension (str): File extension without the dot
        
    Returns:
        str: Category name or "Misc" if not found
    """
    return CATEGORIES.get(extension.lower(), "Misc") 
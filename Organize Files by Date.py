# Repository: python-file-organizer


import os
import shutil
from datetime import datetime

def organize_files_by_date(directory):
    """Organize files into folders based on their creation date."""
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            creation_time = datetime.fromtimestamp(os.path.getctime(filepath)).strftime('%Y-%m-%d')
            folder = os.path.join(directory, creation_time)
            os.makedirs(folder, exist_ok=True)
            shutil.move(filepath, os.path.join(folder, filename))
    print("Files organized by date successfully.")

# Example usage
organize_files_by_date("/path/to/directory")

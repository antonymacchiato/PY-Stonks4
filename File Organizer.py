### **Repository 3: File Organizer**
```python
# Repository: python-file-organizer
# Description: Organize files in a directory by their extensions.

import os
import shutil

def organize_files(directory):
    """Organize files into folders based on their extensions."""
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            ext = filename.split('.')[-1]
            folder = os.path.join(directory, ext)
            os.makedirs(folder, exist_ok=True)
            shutil.move(os.path.join(directory, filename), os.path.join(folder, filename))
    print("Files organized successfully.")

import logging

logging.basicConfig(filename='organizer.log', level=logging.INFO)

def organize_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            ext = filename.split('.')[-1]
            folder = os.path.join(directory, ext)
            os.makedirs(folder, exist_ok=True)
            shutil.move(os.path.join(directory, filename), os.path.join(folder, filename))
            logging.info(f"Moved {filename} to {folder}")
    print("Files organized successfully.")

def organize_files(directory, rule=lambda x: x.split('.')[-1]):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            folder = os.path.join(directory, rule(filename))
            os.makedirs(folder, exist_ok=True)
            shutil.move(os.path.join(directory, filename), os.path.join(folder, filename))
    print("Files organized successfully.")

# Example usage
organize_files("/path/to/directory")

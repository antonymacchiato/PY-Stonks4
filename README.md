
---

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

# Example usage
organize_files("/path/to/directory")

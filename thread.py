import os
import shutil
from threading import Thread

def organize_file(file, directory):
    ext = file.split('.')[-1]
    folder = os.path.join(directory, ext)
    os.makedirs(folder, exist_ok=True)
    shutil.move(os.path.join(directory, file), os.path.join(folder, file))

def organize_files(directory):
    threads = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            thread = Thread(target=organize_file, args=(filename, directory))
            threads.append(thread)
            thread.start()
    for thread in threads:
        thread.join()
    print("Files organized successfully.")

# Example usage
organize_files("/path/to/directory")

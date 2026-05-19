# Python file detection

import os # imports operating system module

file_path = "oop/fileHandling" # relative file path

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a folder/directory")
else:
    print("That location doesn't exist")
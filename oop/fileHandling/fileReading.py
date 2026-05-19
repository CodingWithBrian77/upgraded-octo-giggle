# Python reading files (.txt, .json, .csv)
 
import json
import csv

file_path1 = "oop/fileHandling/input.txt"
file_path2 = "oop/fileHandling/input.json"
file_path3 = "oop/fileHandling/input.csv"

try:
    with open(file_path1, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")

try:
    with open(file_path2, "r") as file:
        content = json.load(file)
        print(content["job"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")

try:
    with open(file_path3, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[2])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")
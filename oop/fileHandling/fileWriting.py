# Python writing files (.txt, .json, .csv)
import json # must import json module to access json methods
import csv # must import csv module to access csv methods

employees1 = ["Eugene", "Squidward", "Spongebob", "Patrick"]

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

employees2 = [["Name", "Age", "Job"],
              ["Spongebob", 30, "Cook"],
              ["Patrick", 37, "Unemployed"],
              ["Sandy", 27, "Scientist"]
              ]

file_path1 = "oop/fileHandling/output.txt"
file_path2 = "oop/fileHandling/output.json"
file_path3 = "oop/fileHandling/output.csv"

# -- WRITING TXT FILES -- #
# try:
    # with open(file=file_path1, mode= "w") as file:
        # for employee in employees:
            # file.write(employee + "\n")
        # print(f"txt file '{file_path1}' was created")
# except FileExistsError:
    # print("That file already exists!")

# -- WRITING JSON FILES -- #
# try:
    # with open(file_path2, "w") as file:
        # json.dump(employee, file, indent=4)
        # print(f"json file '{file_path2}' was created")
# except FileExistsError:
    # print("That file already exists")

# -- WRITING CSV FILES -- #
try:
    with open(file_path3, "w", newline = "") as file:
        writer = csv.writer(file)
        for row in employees2:
            writer.writerow(row)
        print(f"csv file '{file_path3}' was created")
except FileExistsError:
    print("That file already exists")
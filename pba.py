import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Students who scored above 75:")
    for row in reader:
        if float(row["Marks"]) > 75:
            print("Name:", row["Name"], "Marks:", row["Marks"])

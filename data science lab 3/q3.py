import csv

try:
    file = open("students.csv", "r")
    reader = csv.reader(file)

    next(reader)   # skip header

    print("Roll\tName\tMarks")

    for row in reader:
        try:
            print(row[0], "\t", row[1], "\t", row[2])
        except:
            pass   # ignore wrong rows

    file.close()

except:
    print("File not found or error in reading file")
    
import json

file_name = "students.json"

try:
    with open(file_name, "r") as file:
        try:
            data = json.load(file)  # Load JSON data
        except json.JSONDecodeError:
            print("Error: File content is not valid JSON.")
            data = []

    if data:  # Check if data is not empty
        for student in data:
            print(f"ID: {student.get('id')}, Name: {student.get('name')}, Marks: {student.get('marks')}")
    else:
        print("No student data found in the file.")

except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: Cannot read the file.")



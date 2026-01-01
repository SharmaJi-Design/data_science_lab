# Writing multiple lines to a file
file_name = "sample.txt"

with open(file_name, "w") as file:
    file.write("Hello, this is a first line of file handling.\n")
    file.write("This is a second line of file handling.\n")
    file.write("This is the third line of file handling.\n")

print("Data written to the file successfully.")

# Reading the file content 
file_name = "sample.txt"

with open(file_name, "r") as file:
    content = file.read()
    print("\nFile Contents:")
    print(content)

# Handling file not found using try–except
try:
    with open("Non_existing_file.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: File not found. Please check the file name.")




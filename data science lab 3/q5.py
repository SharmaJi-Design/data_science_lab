file_name = "data.txt"

while True:
    print("\n--- File Menu ---")
    print("1. Write data to file")
    print("2. Read data from file")
    print("3. Append data to file")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = input("Enter data to write: ")
            with open(file_name, "w") as file:
                file.write(data + "\n")
            print("Data written successfully.")

        elif choice == 2:
            with open(file_name, "r") as file:
                print("\nFile Contents:")
                print(file.read())

        elif choice == 3:
            data = input("Enter data to append: ")
            with open(file_name, "a") as file:
                file.write(data + "\n")
            print("Data appended successfully.")

        elif choice == 4:
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select 1–4.")

    except ValueError:
        print("Invalid input! Please enter a number.")

    except FileNotFoundError:
        print("Error: File not found.")

    except IOError:
        print("Error: An I/O error occurred.")

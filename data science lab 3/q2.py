# Reading numbers from a file, calculating sum and average, ignoring invalid entries.
file_name = "numbers.txt"

total = 0
count = 0

try:
    with open(file_name, "r") as file:
        for line in file:
            try:
                number = float(line)
                total += number
                count += 1
            except ValueError:
                # Ignore invalid entries
                pass

    if count > 0:
        average = total / count
        print("Sum of valid numbers:", total)
        print("Average of valid numbers:", average)
    else:
        print("No valid numbers found.")

except FileNotFoundError:
    print("Error: File not found.")

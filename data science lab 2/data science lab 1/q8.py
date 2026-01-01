# 8. Write a program that checks if a year is a leap year. 
def leap_year():
    year = input("Enter the year: ")

    if year.isdigit():
        year = int(year)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Invalid input!")

leap_year()
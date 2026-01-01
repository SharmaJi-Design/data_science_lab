# 1. Write a program that takes two numbers as input from the user, and print their sum. 
def add_number():
    num1 = input("Enter the 1st number: ")
    num2 = input("Enter the 2nd number: ")

    if num1.isdigit() and num2.isdigit():
        print("Sum =", int(num1) + int(num2))
    else:
        print("Invalid input! Please enter numbers only.")
        

add_number()
# 6. Write a program that checks if a given number is even or odd. 
def even_odd():
    n = input("Enter the number: ")

    if int (n) % 2 == 0:
        print("Even Number")
    else:
        print("odd number")

even_odd()
#7. Write a program that takes a list of numbers as input, and returns the largest number in the list. 
def largest_num():
    num = input("Enter the numbers: ").split()
    largest = int(num[0])

    for n in num:
        n = int(n)
        if n > largest:
            largest = n

    print("Largest Number:", largest)

largest_num()
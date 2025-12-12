# 2.  Write a program that checks if a given string is palindrome.
def Palindrome_number():
    s=input("Enter the string: ")
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

Palindrome_number()
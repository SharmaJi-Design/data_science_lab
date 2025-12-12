# 4. Write a python program that prints the Fibonacci series up to n terms.
def fibonacci():
    n = input("how many term: ")

    if not n.isdigit():
        print("invalid input!")
        return
    
    n = int(n)
    a , b = 0 , 1
    for _ in range(n):
        print(a, end=" ")
        a , b = b , a+b

fibonacci()
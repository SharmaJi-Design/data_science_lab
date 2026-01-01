# 3. Write a program that prints all prime numbers up to a given number ‘n’. 
def prime_upto_n():
    n = input("Enter number: ")

    if not n.isdigit():
        print("Invalid input")
        return
    
    n = int(n)
    print("Prime numbers up to", n, ":")

    for i in range(2, n+1):
        isprime = True
        for j in range(2, int(i**0.5)+1):  # optimization: check up to sqrt(i)
            if i % j == 0:
                isprime = False
                break
        if isprime:
            print(i, end=" ")

prime_upto_n()
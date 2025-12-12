# 5. Define a function that takes two numbers as arguments, and returns their greatest 
#common divisor (GCD).
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


result = gcd(12, 18)
print("GCD:", result)
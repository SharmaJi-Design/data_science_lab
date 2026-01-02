# Generator function to produce numbers from 1 to 5
def generate_numbers():
    for num in range(1, 6):
        yield num  
numbers = generate_numbers()

print("The generate a number 1 to 5 :")
for number in numbers:
    print(number)        
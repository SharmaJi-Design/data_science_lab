# 9. Write a program that takes a temperature in Celsius, and converts it to Fahrenheit and Kelvin, based on the choice of user.
def temperature_convert():
    c = input("Enter the temerature in celsius: ")

    if c.replace('.',' ',1).isdigit():
        c = float(c)
        print("1.Fahrenheit.2.kelvin")
        choice = input("Enter choice: ")

        if choice =='1':
            print("fahrenheit",(c*9/5)+32)
        elif choice == '2':
            print("kelvin",c+273.15)
        else:
            print("invalid choice")
    else:
        print("invalid temperature!")

temperature_convert()
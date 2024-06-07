print("**************** Calculator ****************")
print("\n")

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
print( "Enter 1 for Addition \t 2 for Subtraction \t 3 for multiply \t 3 for division")
option = int(input("Enter the option"))
if option == 1:
    print("Addition of these number =", num1 + num2)

elif option == 2:
    print("Subtraction=",num1 - num2)

elif option == 3:
    print("Multiply=",num1 * num2)

elif option == 4:
    print("Division=",num1 / num2)


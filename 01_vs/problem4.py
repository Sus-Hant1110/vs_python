# Problem:4
# Wap to make a calculator using functions

# Solution:

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def calculator():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter the choice: "))

    if choice == 1:
        print("Addition:", add(a, b))
    elif choice == 2:
        print("Subtraction:", sub(a, b))
    elif choice == 3:
        print("Multiplication:", mul(a, b))
    elif choice == 4:
        print("Division:", div(a, b))
    else:
        print("Invalid choice")

calculator()

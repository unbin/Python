def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

opperation = 0
num1 = 0
num2 = 0
result = 0

while(1):
    # Select opperation
    print("\n1. +\n2. -\n3. *\n4. /\n")
    print("Select an opperation: ")
    usr = float(input())

    # Input numbers
    print("Enter the first number: ")
    num1 = float(input())
    print("Enter the second number: ")
    num2 = float(input())

    if usr == 1:
        result = add(num1, num2)
    elif usr == 2:
        result = sub(num1, num2)
    elif usr == 3:
        result = mul(num1, num2)
    elif usr == 4:
        result = div(num1, num2)
    else:
        print("failed")

    print("Result: {:g}".format(result))

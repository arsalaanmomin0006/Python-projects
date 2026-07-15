def add(a, b):
    print(a + b)
    
def subtract(a, b):
    print(a - b)

def multiply(a, b):
    print(a *b)

def divide(a, b):
    print(a / b)

while True:
    F_n = int(input("Enter first no:"))
    S_n = int(input("Enter second no:"))
    operation = input("Enter what operation to do(+, -, *, /):")

    if operation == "+":
        add(F_n, S_n)
    elif operation == "-":
        subtract(F_n,  S_n)
    elif operation == "*":
        multiply(F_n, S_n)
    elif operation == "/":
        if S_n == 0:
            print("Cannot divide by zero")
        else:
            divide(F_n, S_n)
    else:
        print("Invalid Operation")

    A_n = input("Want to continue the calculation? Answer Yes or No:")
    if A_n == "No":
        break

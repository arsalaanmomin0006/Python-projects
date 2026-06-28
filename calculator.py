while True:
    F_n = int(input("Enter first no:"))
    S_n = int(input("Enter second no:"))
    operation = input("Enter what operation to do(+, -, *, /):")

    if operation == "+":
        print(F_n + S_n)
    elif operation == "-":
        print(F_n - S_n)
    elif operation == "*":
        print(F_n * S_n)
    elif operation == "/":
        if S_n == "0":
            print("Cannot divide by zero")
        else:
            print(F_n / S_n)

    A_n = input("Want to continue the calculation? Answer Yes or No:")
    if A_n == "No":
        break

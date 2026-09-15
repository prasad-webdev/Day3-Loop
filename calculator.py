A = int(input("Enter first no : "))
op = input("Enter operator (+, -, *, /): ")
B = int(input("Enter second no  "))
if op == "+":
    print(f"Result: {A + B}")
elif op == "-":
    print(f"Result: {A - B}")
elif op == "*":
    print(f"Result: {A * B}")
elif op == "/":
    print(f"Result: {A / B}")
    if num2 == 0:
        print("Error: Cannot divide by zero")
    else:
        print(f"Result: {A / B}")
else:
    print("Invalid operator entered")


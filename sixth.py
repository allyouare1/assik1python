first = int(input("First number: "))
operation = input("Operation: ")
second = int(input("Second number: "))
if operation == "+":
    result = first + second
elif operation == "-":
    result = first - second
elif operation == "*":
    result = first * second
elif operation == "/":
    result = first / second
else:
    print("Unknown sign")
    result = 0
if result > 0 :
    print(f"{first} {operation} {second} = {result}")
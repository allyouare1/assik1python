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
    result = first / second if second !=0 else "Error"
else:
    print("Unknown sign")
    result = None 
if result != None  :
    print(f"{first} {operation} {second} = {result}")
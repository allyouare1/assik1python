equation = input().strip()
unknown = 0
if len(equation) == 5:
    first = equation[0]
    op = equation[1]
    third = equation[2]
    fourth = equation[3]
    fifth = equation[4]

    if fourth != "=":
        print("format error")
    else:
        if first == "x":

            t= int(third)
            f = int(fifth)
            if op == "+":
                unknown = f - t
            elif op == "-":
                unknown = f + t
            else:
                print("there is no plus/minus")
        elif third == "x":
           
            fi = int(first)
            f = int(fifth)
            if op == "+":
                unknown = f - fi
            elif op == "-":
                unknown = fi - f
            else:
                print("there is no plus/minus")
        else:
            print("there is  no unknown")

print(unknown)

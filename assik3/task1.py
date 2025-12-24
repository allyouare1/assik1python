print("write down your shape")
print("square/rectangle - a" )
print ("triangle - b")
print ("circle - c")
shape=input()
area=0
if shape=="a":
    print("give your hight and base")
    hight=input()
    base=input()
    area=int(hight)*int(base)
elif shape=="b":
    print("give your base and hight")
    base=input()
    hight=input()
    area=(int(base)*int(hight))*(1/2)
elif shape=="c":
    print("give your radius")
    radius=input()
    area=3.14*(int(radius)^2)
print(shape)
print(f"your area is:{area}")

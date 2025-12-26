l1=int(input()) 
l2=int(input())
s1=int(input())
s2=int(input()) 
h1=(l1**2+l2**2)**0.5
h2=(s1**2+s2**2)**0.5
if h1>h2:
    print(h1,"is greter than",h2)
elif h2>h1:
    print(h2,"is greter than",h1)
else:
    print("Both are equal")
print("first hypotenuse:",h1)
print("second hypotenuse:",h2)


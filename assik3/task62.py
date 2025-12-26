a = int(input())
b = int(input())
c=int(input())
d=int(input())
diagonal=int(input())
p1=(a+b+diagonal)/2
p2=(c+d+diagonal)/2
s1=(p1*(p1 - a)*(p1 - b)*(p1 - diagonal))**0.5
s2=(p2*(p2 - c)*(p2 - d)*(p2 - diagonal))**0.5
s=s1+s2
print("area is:",s)
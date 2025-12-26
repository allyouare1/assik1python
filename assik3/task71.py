a=int(input())
b=int(input())
c=int(input())
d=int(input())
s1=(a+b)/2
diagonal=(a**2+b**2)**0.5
p=(c+d+diagonal)/2
s2=(p*(p - c)*(p - d)*(p - diagonal))**0.5
s=s1+s2
print("area is:",s)
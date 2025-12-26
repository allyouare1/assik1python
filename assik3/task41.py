A = int(input())
B = int(input())
C = int(input())
D = int(input()) 
usti=A*D
asty=B*C
u=usti
a=asty
while a !=0:
    temp_u=u
    temp_a=a
    u=temp_a
    a=temp_u%temp_a
g=u
print("gcd is:",g)
u2=usti/g
a2=asty/g
print(u2,"/",a2)

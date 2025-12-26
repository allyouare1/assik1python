A = int(input())
B = int(input())
C = int(input())
D = int(input())  
usti=A*D-C*B
asty=B*D
if usti != 0 and asty !=0:
    usti_original = usti
    if usti>0:
        usti_n=usti
    else:
        usti_n=-(usti)
    u=usti_n
    a=asty
    while a !=0:
        temp_u=u
        temp_a=a
        u=temp_a
        a=temp_u%temp_a
    g=u
    usti2=usti_original//g
    asty2=asty//g
    print(usti2,"/",asty2)
elif usti==0:
    print("0")
elif asty==0:
    print("error")
else:
    print("undefined")
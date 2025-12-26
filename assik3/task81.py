num=input()
n=int(num)
for number in range(1,n+1):
    div=True
    number_str = str(number)
    for  char in number_str: 
        d=int(char)
        if d==0 or number % d !=0:
            div=False
            break
    if div:
        print(number,end=' ')

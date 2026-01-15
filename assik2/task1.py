put=input()
count=0
for i in range  (len(put)):
    if (put[i]== ">"and  put[i+1]==">" and  put[i+2]=="-" and put[i+3]=="-" and put[i+4]==">"):
        count+=1
    elif (put[i]== "<" and  put[i+1]=="-" and  put[i+2]=="-" and put[i+3]=="<" and  put[i+4]=="<"):
        count+=1
print (count)

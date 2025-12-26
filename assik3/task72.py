number=int(input())
octal= ""
temp_number=number
if number==0:
    octal="0"
else:
    while temp_number>0:
        remainder=temp_number%8
        octal=str(remainder)+octal
        temp_number//=8
while len(octal)<10:
    octal="0"+octal
print(octal)

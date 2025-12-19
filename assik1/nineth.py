ticket=(input("Enter your ticket number:"))
if len(ticket)==6:
        first=int(ticket[0])
        second=int(ticket[1])
        third=int(ticket[2])
        fourth=int(ticket[3])
        fifth=int(ticket[4])
        sixth=int (ticket[5])
        if(first+ second +third )==(fourth + fifth + sixth):
                print("YES")
        else:
                print("NO")
    
else:
            print(f"Error: Please enter exactly 6 numbers")
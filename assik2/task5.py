check = int(input())
letters = ['A', 'B', 'C', 'E', 'H', 'K', 'M', 'O', 'P', 'T', 'X', 'Y']
for _ in range(check):
    platenumber = input().strip()
    if (len(platenumber) == 6 and
        platenumber[0] in letters and
        platenumber[1].isdigit() and
        platenumber[2].isdigit() and
        platenumber[3].isdigit() and
        platenumber[4] in letters and
        platenumber[5] in letters):
        print("Yes")
    else:
        print("No")
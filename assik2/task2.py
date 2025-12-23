first = input().strip()  
second = input().strip() 
f= len(first)
s = len(second)

    
cycle = []

for k in range(s):
       shift= second[k:] + second[:k]
       if shift not in cycle:
            cycle.append(shift)

count = 0

for i in range(f - s + 1):
        sub = first[i:i+s]  
        if sub in cycle:
            count += 1

  
print(count)
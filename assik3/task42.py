a = int(input())
b = int(input())

R = int(input())

p1 = int(input())
p2 = int(input())

f1 = int(input())
f2 = int(input())

l1 = int(input())
l2 = int(input())
counter=0

if (p1 - a)**2 + (p2 - b)**2 <= R**2:
    counter += 1

if (f1 - a)**2 + (f2 - b)**2 <= R**2:
    counter += 1

if (l1 - a)**2 + (l2 - b)**2 <= R**2:
    counter += 1

print("points inside:", counter)
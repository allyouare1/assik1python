n=int(input())
array = []
for i in range(n):
    x = int(input())
    array.append(x)
print("Initial array:", array)
if n > 1:
    temp = array[0]
    array[0] = array[n - 1]
    array[n - 1] = temp
print("After array:", array)
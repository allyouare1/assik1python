a = int(input())
b = int(input())
ainitial=a
binitial=b
while b != 0:
    temp_a = a
    temp_b = b
    a = temp_b
    b = temp_a % temp_b
g = a
l = (ainitial * binitial) // g
print("gcd is:", g)
print("lcm is:", l)
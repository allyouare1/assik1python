f, s = map(int, input().split())
t = input().strip()
w = set()
for i in range(f - s + 1):
    sub = t[i:i+s]
    w.add(sub)
print(len(w))
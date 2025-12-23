l = ["one", "two", "three"]
max = 0
for i in l:
        if len(i) > max:
            max = len(i)

new = []
for i in l:
        while len(i) < max:
            i = i + "_"
        new.append(i)
print(new)
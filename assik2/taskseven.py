l = input().strip()
items = l.split()

f = {}
for item in items:
    if item in f:
        f[item] += 1
    else:
        f[item] = 1

print("Purchase frequency:")
for item, count in f.items():
    print(f"{item}: {count}")

m_items= None
m_count = 0
for item, count in f.items():
    if count > m_count:
        m_count = count
        m_item = item

print("Most popular item:", m_item)

o_items = []
for item, count in f.items():
    if count == 1:
        o_items.append(item)
print("Purchased once:", " ".join(o_items))

sorted = list(f.items())
sorted.sort(key=lambda pair: pair[1], reverse=True)

print("Sorted by frequency:")
for item, count in sorted:
    print(item, count)
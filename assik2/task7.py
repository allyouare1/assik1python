line = input().strip()
items = line.split()

freq = {}
for item in items:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print("Purchase frequency:")
for item, count in freq.items():
    print(f"{item}: {count}")

m_item = None
m_count = 0
for item, count in freq.items():
    if count > m_count:
        m_count = count
        m_item = item

print("Most popular item:", m_item)

o_items = []
for item, count in freq.items():
    if count == 1:
        o_items.append(item)

print("Purchased once:", " ".join(o_items))

sorted = list(freq.items())
sorted.sort(key=lambda pair: pair[1], reverse=True)

print("Sorted by frequency:")
for item, count in sorted:
    print(item, count)
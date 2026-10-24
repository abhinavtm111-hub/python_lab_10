d1 = {"apple": 3, "banana": 5, "orange": 2}
d2 = {"grape": 4, "mango": 6}

print("Dictionary 1:", d1)
print("Sorted dictionary:", dict(sorted(d1.items())))

merged = {**d1, **d2}
print("Merged dictionary:", merged)

text = input("Enter a string: ")
frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

print("Character frequency:", frequency)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Common elements:", set1 & set2)
print("Unique elements in set1:", set1 - set2)
print("Unique elements in set2:", set2 - set1)
print("All unique elements:", set1 ^ set2)
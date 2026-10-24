s = input("Enter a string: ")

old = input("Enter character to replace: ")
new = input("Enter new character: ")
print("After replacement:", s.replace(old, new))

print("Reversed string:", s[::-1])

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

char = input("Enter character to count: ")
print("Character frequency:", s.count(char))

words = s.split()
print("Word frequencies:")
for word in set(words):
    print(word, ":", words.count(word))
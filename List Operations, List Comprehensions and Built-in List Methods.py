numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

numbers.append(60)
print("After append:", numbers)

numbers.insert(2, 25)
print("After insert:", numbers)

numbers.remove(40)
print("After remove:", numbers)

if 30 in numbers:
    print("30 found in the list")

numbers[0] = 5
print("After update:", numbers)

even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)

squares = [x * x for x in numbers]
print("Squares:", squares)

numbers.sort()
print("Sorted list:", numbers)

numbers.reverse()
print("Reversed list:", numbers)
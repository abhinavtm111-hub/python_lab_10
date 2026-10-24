values = input("Enter comma-separated numbers: ")
numbers = values.split(",")

numbers_tuple = tuple(numbers)

print("List:", numbers)
print("Tuple:", numbers_tuple)
print("Total number of elements:", len(numbers))
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Reverse list:", numbers[::-1])
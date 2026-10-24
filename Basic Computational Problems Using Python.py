import math

r = float(input("Enter radius of circle: "))
area = math.pi * r * r
print("Area of circle:", area)

year = int(input("Enter year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

largest = max(a, b, c)
print("Largest number:", largest)

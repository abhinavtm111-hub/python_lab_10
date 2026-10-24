def total_marks(marks):
    return sum(marks)

def average_marks(marks):
    return sum(marks) / len(marks)

def highest_marks(marks):
    return max(marks)

def lowest_marks(marks):
    return min(marks)

def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks: ").split()))

    total = total_marks(marks)
    average = average_marks(marks)
    highest = highest_marks(marks)
    lowest = lowest_marks(marks)
    student_grade = grade(average)

    students.append({
        "name": name,
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "grade": student_grade
    })

students.sort(key=lambda x: x["total"], reverse=True)

print("\nStudent Performance")

for student in students:
    print("Name:", student["name"])
    print("Total:", student["total"])
    print("Average:", student["average"])
    print("Highest:", student["highest"])
    print("Lowest:", student["lowest"])
    print("Grade:", student["grade"])
    print()
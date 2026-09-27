student = {
    "Name": "Rahul",
    "Age": 20,
    "Course": "Python"
}

print("Original Dictionary:", student)

print("1. Access Name:", student["Name"])

student["Grade"] = "A"
print("2. After Adding:", student)

student["Age"] = 21
print("3. After Updating:", student)

print("4. After pop():", student)

print("5. Using get():", student.get("Name"))

print("6. Keys:", student.keys())

print("7. Values:", student.values())

print("8. Items:", student.items())

student_copy = student.copy()
print("9. Copied Dictionary:", student_copy)

student.clear()
print("10. After clear():", student)

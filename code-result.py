# Take input from user
student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))
student_grades = list(
    map(int, input("Enter your grades separated by commas: ").split(","))
)

# Calculate average
average_grade = sum(student_grades) / len(student_grades)

# Check passing condition
is_passing = average_grade >= 75

# Display output
print("\nStudent Name:", student_name)
print("Student Age:", student_age)
print("Student Grades:", student_grades)
print("Average Grade:", round(average_grade, 2))

if is_passing:
    print("Student is passing.")
else:
    print("Student is not passing.")

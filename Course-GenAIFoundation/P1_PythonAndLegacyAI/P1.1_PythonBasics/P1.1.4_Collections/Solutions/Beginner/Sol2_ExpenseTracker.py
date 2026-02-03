"""
Beginner Solution 2: Student Grade Calculator
"""

# Input data
grades_str = "85, 92, 78, 95, 88"

# Parse into list
grades = [int(g.strip()) for g in grades_str.split(',')]

# Calculate statistics
total = sum(grades)
average = total / len(grades)
num_subjects = len(grades)

print(f"Grades: {grades}")
print(f"Total score: {total}")
print(f"Average score: {average:.2f}")
print(f"Number of subjects: {num_subjects}")

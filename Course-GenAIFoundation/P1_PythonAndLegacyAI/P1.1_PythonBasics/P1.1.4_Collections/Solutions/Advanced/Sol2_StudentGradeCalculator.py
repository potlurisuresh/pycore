"""
Advanced Solution 2: Student Grade Calculator
"""

# Input data
grade_matrix = """Student,Math,Science,English,History
Alice,85,92,78,88
Bob,65,72,58,70
Carol,95,88,92,90
David,55,62,58,65
Eve,88,85,90,87"""

# Parse matrix
lines = grade_matrix.strip().split('\n')
headers = lines[0].split(',')
subjects = headers[1:]  # Skip 'Student' column

students = []
matrix = []

for line in lines[1:]:
    parts = line.split(',')
    student_name = parts[0]
    grades = [int(g) for g in parts[1:]]
    students.append(student_name)
    matrix.append(grades)

# Calculate student averages (rows)
student_avgs = {students[i]: sum(matrix[i]) / len(matrix[i]) for i in range(len(students))}

# Calculate subject averages (columns)
subject_avgs = {}
for j in range(len(subjects)):
    col_sum = sum(matrix[i][j] for i in range(len(students)))
    subject_avgs[subjects[j]] = col_sum / len(students)

# Grade distribution
def get_letter(score):
    if score >= 90: return 'A'
    if score >= 80: return 'B'
    if score >= 70: return 'C'
    if score >= 60: return 'D'
    return 'F'

distribution = {}
for row in matrix:
    for grade in row:
        letter = get_letter(grade)
        distribution[letter] = distribution.get(letter, 0) + 1

print("Student Averages:")
for name, avg in student_avgs.items():
    print(f"{name}: {avg:.2f}")

print("\nSubject Averages:")
for subj, avg in subject_avgs.items():
    print(f"{subj}: {avg:.2f}")

print("\nGrade Distribution:")
for grade in ['A', 'B', 'C', 'D', 'F']:
    count = distribution.get(grade, 0)
    print(f"{grade}: {count}")

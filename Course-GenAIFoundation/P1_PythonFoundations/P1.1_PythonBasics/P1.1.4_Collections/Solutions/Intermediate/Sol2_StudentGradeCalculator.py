"""
Intermediate Solution 2: Student Grade Calculator
"""

# Input data
student_data = """Alice:85,92,78
Bob:65,58,72
Carol:95,88,92
David:55,62,58"""

# Process students
students = []
all_scores = []

for line in student_data.split('\n'):
    name, grades_str = line.split(':')
    grades = [int(g) for g in grades_str.split(',')]
    average = sum(grades) / len(grades)
    passed = average >= 70
    
    students.append({
        'name': name,
        'grades': grades,
        'average': average,
        'passed': passed
    })
    
    all_scores.extend(grades)

# Calculate class statistics
class_avg = sum(all_scores) / len(all_scores)
highest = max(all_scores)
lowest = min(all_scores)
passed_count = sum(1 for s in students if s['passed'])
pass_rate = (passed_count / len(students)) * 100

print("Student Results:")
for s in students:
    status = "PASS" if s['passed'] else "FAIL"
    print(f"{s['name']}: {s['average']:.2f} - {status}")

print(f"\nClass Statistics:")
print(f"Class average: {class_avg:.2f}")
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")
print(f"Pass rate: {pass_rate:.1f}%")

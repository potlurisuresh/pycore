"""
Solution: Advanced Assignment 4 - Adaptive Learning Assessment (Concise)
"""

question_bank = [
    {"id": 1, "difficulty": "easy", "category": "Math", "max_points": 10, "correct_answer": "A"},
    {"id": 2, "difficulty": "medium", "category": "Math", "max_points": 15, "correct_answer": "B"},
    {"id": 3, "difficulty": "hard", "category": "Math", "max_points": 20, "correct_answer": "C"},
    {"id": 4, "difficulty": "easy", "category": "Science", "max_points": 10, "correct_answer": "A"},
    {"id": 5, "difficulty": "medium", "category": "Science", "max_points": 15, "correct_answer": "B"},
    {"id": 6, "difficulty": "hard", "category": "Science", "max_points": 20, "correct_answer": "C"},
    {"id": 7, "difficulty": "easy", "category": "English", "max_points": 10, "correct_answer": "D"},
    {"id": 8, "difficulty": "medium", "category": "English", "max_points": 15, "correct_answer": "A"},
    {"id": 9, "difficulty": "hard", "category": "English", "max_points": 20, "correct_answer": "B"},
]

student_attempts = [
    {"question_id": 1, "answer": "A", "time_spent": 25, "confidence": 5},
    {"question_id": 2, "answer": "B", "time_spent": 45, "confidence": 4},
    {"question_id": 3, "answer": "C", "time_spent": 60, "confidence": 3},
    {"question_id": 4, "answer": "A", "time_spent": 20, "confidence": 5},
    {"question_id": 5, "answer": "B", "time_spent": 40, "confidence": 2},
    {"question_id": 6, "answer": "D", "time_spent": 90, "confidence": 2},
    {"question_id": 7, "answer": "D", "time_spent": 15, "confidence": 5},
    {"question_id": 8, "answer": "A", "time_spent": 35, "confidence": 4},
    {"question_id": 9, "answer": "B", "time_spent": 70, "confidence": 2},
]

mastery_threshold = 80.0
question_map = {q["id"]: q for q in question_bank}

category_stats = {}
total_points = 0
total_max = 0
time_accuracy = []
confidence_accuracy = []

for attempt in student_attempts:
    q = question_map[attempt["question_id"]]
    correct = attempt["answer"] == q["correct_answer"]
    points = q["max_points"] if correct else 0
    total_points += points
    total_max += q["max_points"]

    time_accuracy.append((attempt["time_spent"], 1 if correct else 0))
    confidence_accuracy.append((attempt["confidence"], 1 if correct else 0))

    stats = category_stats.setdefault(q["category"], {"points": 0, "max": 0, "count": 0})
    stats["points"] += points
    stats["max"] += q["max_points"]
    stats["count"] += 1

overall_pct = (total_points / total_max) * 100

print("Adaptive Learning Report")
print("=" * 48)
print(f"Overall Score: {total_points}/{total_max} ({overall_pct:.1f}%)")

print("\nCategory Mastery:")
weak_categories = []
for category, stats in category_stats.items():
    pct = (stats["points"] / stats["max"]) * 100
    status = "Mastered" if pct >= mastery_threshold else "Needs Review"
    if pct < mastery_threshold:
        weak_categories.append(category)
    print(f"- {category}: {pct:.1f}% ({status})")

high_conf = [a for c, a in confidence_accuracy if c >= 4]
low_conf = [a for c, a in confidence_accuracy if c <= 2]
high_conf_acc = (sum(high_conf) / len(high_conf) * 100) if high_conf else 0
low_conf_acc = (sum(low_conf) / len(low_conf) * 100) if low_conf else 0

print("\nConfidence vs Accuracy:")
print(f"- High confidence (4-5): {high_conf_acc:.0f}%")
print(f"- Low confidence (1-2): {low_conf_acc:.0f}%")

print("\nRecommendations:")
if weak_categories:
    print("- Focus on: " + ", ".join(weak_categories))
print("- Review low-confidence questions")
print("- Attempt harder items in mastered categories")
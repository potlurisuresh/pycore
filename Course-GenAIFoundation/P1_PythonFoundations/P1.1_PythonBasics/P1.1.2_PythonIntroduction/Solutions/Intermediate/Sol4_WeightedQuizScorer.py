"""
Solution: Intermediate Assignment 4 - Weighted Quiz Scorer (Concise)
"""

# Input data
questions = [
    {"id": 1, "max_points": 20},
    {"id": 2, "max_points": 30},
    {"id": 3, "max_points": 50},
]

user_answers = [
    {"question_id": 1, "points_earned": 18},
    {"question_id": 2, "points_earned": 21},
    {"question_id": 3, "points_earned": 40},
]

passing_percentage = 70.0

# Step 1-3: Match answers to questions and calculate percentages
total_points = 0
total_max = 0
question_results = []

print("Question Performance:")
print("-" * 50)

for answer in user_answers:
    q_id = answer["question_id"]
    points_earned = answer["points_earned"]
    
    # Find corresponding question
    question = next((q for q in questions if q["id"] == q_id), None)
    max_points = question["max_points"]
    percentage = (points_earned / max_points) * 100
    
    total_points += points_earned
    total_max += max_points
    
    question_results.append({
        "id": q_id,
        "earned": points_earned,
        "max": max_points,
        "percentage": percentage
    })
    
    print("Q{}: {}/{} ({:.1f}%)".format(q_id, points_earned, max_points, percentage))

# Step 4-5: Calculate overall percentage
overall_percentage = (total_points / total_max) * 100

print("-" * 50)
print("Total: {}/{} ({:.1f}%)".format(total_points, total_max, overall_percentage))

# Step 6: Determine performance level
if overall_percentage >= 90:
    performance = "Excellent"
elif overall_percentage >= 80:
    performance = "Good"
elif overall_percentage >= passing_percentage:
    performance = "Fair"
else:
    performance = "Poor"

print("Performance: {}".format(performance))

# Step 7: Identify questions below 50%
weak_questions = [q for q in question_results if q["percentage"] < 50]

print("\nQuestions Below 50%:")
if weak_questions:
    for q in weak_questions:
        print("  Q{}: {:.1f}%".format(q['id'], q['percentage']))
else:
    print("  None - Great job!")


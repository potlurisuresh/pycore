"""
Solution: Advanced Assignment 4 - Adaptive Learning Assessment System

This solution demonstrates:
- Question bank and attempt tracking
- Per-category aggregation and analysis
- Mastery calculation
- Correlation analysis (time vs accuracy, confidence vs accuracy)
- Personalized recommendation generation
"""

# Question bank (3 categories: Math, Science, English)
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

# Student attempts (final attempt per question)
student_attempts = [
    {"question_id": 1, "answer": "A", "time_spent": 25, "confidence": 5},  # Correct
    {"question_id": 2, "answer": "B", "time_spent": 45, "confidence": 4},  # Correct
    {"question_id": 3, "answer": "C", "time_spent": 60, "confidence": 3},  # Correct
    {"question_id": 4, "answer": "A", "time_spent": 20, "confidence": 5},  # Correct
    {"question_id": 5, "answer": "B", "time_spent": 40, "confidence": 2},  # Correct
    {"question_id": 6, "answer": "D", "time_spent": 90, "confidence": 2},  # Incorrect (lost 20 points)
    {"question_id": 7, "answer": "D", "time_spent": 15, "confidence": 5},  # Correct
    {"question_id": 8, "answer": "A", "time_spent": 35, "confidence": 4},  # Correct
    {"question_id": 9, "answer": "B", "time_spent": 70, "confidence": 2},  # Correct
]

mastery_threshold = 80.0

# Step 1-2: Parse and score attempts
print("QUESTION PERFORMANCE:")
print("-" * 80)

category_stats = {}
total_points = 0
total_max = 0
time_accuracy_data = []
confidence_accuracy_data = []

for attempt in student_attempts:
    q_id = attempt["question_id"]
    question = next(q for q in question_bank if q["id"] == q_id)
    
    is_correct = attempt["answer"] == question["correct_answer"]
    points = question["max_points"] if is_correct else 0
    category = question["category"]
    
    total_points += points
    total_max += question["max_points"]
    
    # Track for correlation analysis
    accuracy = 1 if is_correct else 0
    time_accuracy_data.append((attempt["time_spent"], accuracy))
    confidence_accuracy_data.append((attempt["confidence"], accuracy))
    
    # Aggregate by category
    if category not in category_stats:
        category_stats[category] = {
            "points": 0,
            "max": 0,
            "attempts": 0,
            "correct": 0,
        }
    
    category_stats[category]["points"] += points
    category_stats[category]["max"] += question["max_points"]
    category_stats[category]["attempts"] += 1
    category_stats[category]["correct"] += 1 if is_correct else 0
    
    status = "✓" if is_correct else "✗"
    print("Q{}: {} {:10s} | Points: {:2d}/{:2d} | Time: {:3d}s | Confidence: {}/5".format(q_id, status, category, points, question['max_points'], attempt['time_spent'], attempt['confidence']))

# Step 3: Overall scoring
print("\n" + "=" * 80)
overall_pct = (total_points / total_max) * 100
print("OVERALL SCORE: {}/{} ({:.1f}%)".format(total_points, total_max, overall_pct))
print("=" * 80)

# Step 4: Category breakdown
print("\nCATEGORY BREAKDOWN:")
print("-" * 80)

category_analysis = []
for category, stats in category_stats.items():
    pct = (stats["points"] / stats["max"]) * 100
    mastery_status = "✓ Mastered" if pct >= mastery_threshold else "✗ Below Mastery"
    
    category_analysis.append({
        "category": category,
        "score": pct,
        "points": stats["points"],
        "max": stats["max"],
    })
    
    print("{:12s}: {:2d}/{:2d} ({:5.1f}%) {}".format(category, stats['points'], stats['max'], pct, mastery_status))

# Step 5: Identify weak categories
weak_categories = [c for c in category_analysis if c["score"] < mastery_threshold]

# Step 6: Analyze correlations
print("\nCORRELATION ANALYSIS:")
print("-" * 80)

# Time vs Accuracy: faster = more confident and usually correct
avg_time_correct = sum(t for t, a in time_accuracy_data if a) / sum(1 for t, a in time_accuracy_data if a)
avg_time_incorrect = sum(t for t, a in time_accuracy_data if not a) / sum(1 for t, a in time_accuracy_data if not a)

print("Time Analysis:")
print("  Correct answers: avg {:.0f}s (faster = more confident)".format(avg_time_correct))
print("  Incorrect answers: avg {:.0f}s (slower = uncertain)".format(avg_time_incorrect))

# Confidence vs Accuracy
correct_high_conf = sum(1 for c, a in confidence_accuracy_data if c >= 4 and a)
total_high_conf = sum(1 for c, a in confidence_accuracy_data if c >= 4)
correct_low_conf = sum(1 for c, a in confidence_accuracy_data if c <= 2 and a)
total_low_conf = sum(1 for c, a in confidence_accuracy_data if c <= 2)

print("\nConfidence Analysis:")
print("  High confidence (4-5): {}/{} correct ({:.0f}%)".format(correct_high_conf, total_high_conf, (correct_high_conf/total_high_conf)*100))
print("  Low confidence (1-2): {}/{} correct ({:.0f}%)".format(correct_low_conf, total_low_conf, (correct_low_conf/total_low_conf)*100))

# Step 7: Calculate mastery predictions
print("\nPREDICTED MASTERY:")
print("-" * 80)

mastery_prediction = {}
for cat in category_analysis:
    category = cat["category"]
    score = cat["score"]
    
    if score >= 95:
        mastery = "95% - Ready for certification"
    elif score >= mastery_threshold:
        mastery = "{:.0f}% - Borderline, review recommended".format(score)
    else:
        mastery = "{:.0f}% - Needs more practice".format(score)
    
    mastery_prediction[category] = mastery
    print("{:12s}: {}".format(category, mastery))

# Step 8-9: Generate recommendations
print("\nADAPTIVE RECOMMENDATIONS:")
print("-" * 80)

recommendations = []

# Weak areas
for weak_cat in weak_categories:
    recommendations.append({
        "priority": 1,
        "text": "Focus on {} - Score {:.0f}% (below {:.0f}%)".format(weak_cat['category'], weak_cat['score'], mastery_threshold)
    })

# Low confidence areas
if total_low_conf > 0:
    recommendations.append({
        "priority": 2,
        "text": "Build confidence - {} questions answered with low confidence".format(total_low_conf)
    })

# Challenge areas
recommendations.append({
    "priority": 3,
    "text": "Move to advanced problem sets on mastered topics"
})

# Sort by priority
recommendations.sort(key=lambda x: x["priority"])

for i, rec in enumerate(recommendations[:5], 1):
    print("{i}. {text}".format(i=i, text=rec['text']))

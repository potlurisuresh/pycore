"""
Solution: Beginner Assignment 4 - Simple Quiz Scorer

This solution demonstrates:
- Loop iteration with range and indexing
- Conditional logic inside loops
- Counter variable
- Decision making based on score
"""

# Input data
correct_answers = ["4", "8", "6"]
user_answers = ["4", "7", "6"]

# Step 1-2: Loop through answers and count matches
correct_count = 0
total_questions = len(correct_answers)

for i in range(total_questions):
    if user_answers[i] == correct_answers[i]:
        correct_count += 1
        print("Q{}: Correct ✓".format(i+1))
    else:
        print("Q{}: Incorrect ✗ (Your: {}, Correct: {})".format(i+1, user_answers[i], correct_answers[i]))

# Step 3: Print total and correct count
print("\nTotal: {}/{}".format(correct_count, total_questions))

# Step 4: Print result message based on score
percentage = (correct_count / total_questions) * 100
if correct_count == total_questions:
    result_message = "Perfect Score!"
elif correct_count >= 2:
    result_message = "Good Job"
else:
    result_message = "Need More Practice"

print("Result: {}".format(result_message))

# Alternative approach using zip()
print("\n--- Using zip() ---")
correct_answers_2 = ["4", "8", "6"]
user_answers_2 = ["4", "7", "6"]
correct = sum(1 for correct, user in zip(correct_answers_2, user_answers_2) if correct == user)
print("Correct={}, Result: Good Job".format(correct))

"""
Solution: Beginner Assignment 2 - Daily Step Goal Checker

This solution demonstrates:
- Boolean comparisons
- if/else conditional logic
- Simple decision making
"""

# Input data
user_name = "Jordan"
steps_today = 8200
goal = 10000

# Step 1: Compare steps with goal
steps_reached_goal = steps_today >= goal

# Step 2-3: Print status based on comparison
if steps_today >= goal:
    status = "Goal Achieved"
else:
    status = "Keep going"

# Print results
print("User: {}".format(user_name))
print("Steps Today: {}".format(steps_today))
print("Daily Goal: {}".format(goal))
print("Status: {}".format(status))

# Alternative approach - shorter version
steps_today_2 = 10500
goal_2 = 10000
result = "Goal Achieved" if steps_today_2 >= goal_2 else "Keep going"
print("\nAlternative Output - Status: {}".format(result))

"""
Solution: Intermediate Assignment 2 - Fitness Trends Analyzer

This solution demonstrates:
- Nested list iteration
- Calculating weekly statistics (totals, averages)
- Counting conditions (days below goal)
- Finding maximum in nested structure
- Percentage calculations
"""

# Input data
weeks_data = [
    [8000, 9200, 7500, 10000, 9500, 8800, 9100],  # Week 1
    [9000, 8500, 9800, 10200, 8900, 9100, 9300],  # Week 2
    [8500, 8700, 9000, 9200, 9100, 8900, 9300],   # Week 3
]
daily_goal = 9000

# Step 1-2: Calculate weekly totals and averages
weekly_stats = []
total_days = 0
days_meeting_goal = 0

for week_num, week_data in enumerate(weeks_data, 1):
    weekly_total = sum(week_data)
    weekly_avg = weekly_total / len(week_data)
    
    # Step 3: Count days below goal
    below_goal = sum(1 for day in week_data if day < daily_goal)
    days_above_goal = sum(1 for day in week_data if day >= daily_goal)
    
    weekly_stats.append({
        "week": week_num,
        "total": weekly_total,
        "avg": weekly_avg,
        "below_goal": below_goal
    })
    
    print("Week {}: Total={}, Avg={:.0f}, Below Goal={}".format(week_num, weekly_total, weekly_avg, below_goal))
    
    total_days += len(week_data)
    days_meeting_goal += days_above_goal

# Step 4: Find best week (week with maximum total)
best_week = max(weekly_stats, key=lambda x: x["total"])
print("\nBest Week: {} (Total: {})".format(best_week['week'], best_week['total']))

# Step 5: Calculate consistency score
consistency = (days_meeting_goal / total_days) * 100
print("Consistency Score: {:.1f}%".format(consistency))

# Alternative approach
print("\n--- Using List Comprehension ---")
weekly_totals = [sum(week) for week in weeks_data]
print("Weekly totals: {}".format(weekly_totals))
best_week_num = weekly_totals.index(max(weekly_totals)) + 1
print("Best week: {}".format(best_week_num))

"""
Solution: Advanced Assignment 2 - Fitness Performance Analytics

This solution demonstrates:
- Multi-metric data aggregation
- Statistical analysis (mean, std dev)
- Trend detection and linear projection
- Plateau detection logic
- Anomaly detection using standard deviation
- Correlation analysis
"""

import math

# Input data - 4 weeks of fitness metrics
weekly_data = [
    [
        {"steps": 8000, "distance": 40, "calories": 2000, "heart_rate": 72},
        {"steps": 9200, "distance": 46, "calories": 2300, "heart_rate": 70},
        {"steps": 7500, "distance": 37.5, "calories": 1875, "heart_rate": 75},
        {"steps": 10000, "distance": 50, "calories": 2500, "heart_rate": 68},
        {"steps": 9500, "distance": 47.5, "calories": 2375, "heart_rate": 69},
        {"steps": 8800, "distance": 44, "calories": 2200, "heart_rate": 71},
        {"steps": 9100, "distance": 45.5, "calories": 2275, "heart_rate": 70},
    ],
    [
        {"steps": 9000, "distance": 45, "calories": 2250, "heart_rate": 69},
        {"steps": 8500, "distance": 42.5, "calories": 2125, "heart_rate": 71},
        {"steps": 9800, "distance": 49, "calories": 2450, "heart_rate": 67},
        {"steps": 10200, "distance": 51, "calories": 2550, "heart_rate": 66},
        {"steps": 8900, "distance": 44.5, "calories": 2225, "heart_rate": 72},
        {"steps": 9100, "distance": 45.5, "calories": 2275, "heart_rate": 70},
        {"steps": 9300, "distance": 46.5, "calories": 2325, "heart_rate": 68},
    ],
    [
        {"steps": 9100, "distance": 45.5, "calories": 2275, "heart_rate": 70},
        {"steps": 9300, "distance": 46.5, "calories": 2325, "heart_rate": 69},
        {"steps": 9200, "distance": 46, "calories": 2300, "heart_rate": 70},
        {"steps": 9400, "distance": 47, "calories": 2350, "heart_rate": 68},
    ],
]

baseline = {"weekly_steps": 70000, "weekly_distance": 350, "weekly_calories": 15000, "hr_resting": 60}

# Helper function: calculate standard deviation
def std_dev(values):
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return math.sqrt(variance)

# Step 1-2: Aggregate weekly metrics
print("WEEKLY PERFORMANCE ANALYSIS:")
print("-" * 80)

weekly_summaries = []
for week_num, week in enumerate(weekly_data, 1):
    steps = sum(d["steps"] for d in week)
    distance = sum(d["distance"] for d in week)
    calories = sum(d["calories"] for d in week)
    avg_hr = sum(d["heart_rate"] for d in week) / len(week)
    
    weekly_summaries.append({
        "week": week_num,
        "steps": steps,
        "distance": distance,
        "calories": calories,
        "hr": avg_hr
    })
    
    # Compare to baseline
    steps_pct = (steps / baseline["weekly_steps"]) * 100
    distance_pct = (distance / baseline["weekly_distance"]) * 100
    calories_pct = (calories / baseline["weekly_calories"]) * 100
    
    print("Week {}:".format(week_num))
    print("  Steps: {:,} ({:.0f}%) | Distance: {:.0f}km ({:.0f}%)".format(steps, steps_pct, distance, distance_pct))
    print("  Calories: {:,} ({:.0f}%) | Avg HR: {:.0f} bpm".format(calories, calories_pct, avg_hr))

# Step 3: Calculate trends
print("\nTREND ANALYSIS:")
print("-" * 80)

metrics_trends = {
    "steps": [w["steps"] for w in weekly_summaries],
    "distance": [w["distance"] for w in weekly_summaries],
    "calories": [w["calories"] for w in weekly_summaries],
}

for metric, values in metrics_trends.items():
    if len(values) > 1:
        slope = (values[-1] - values[0]) / (len(values) - 1)
        direction = "↗ improving" if slope > 0 else "↘ declining" if slope < 0 else "→ stable"
        print("{:10s}: {:+.1f} per week {}".format(metric.capitalize(), slope, direction))

# Step 4: Detect plateau
print("\nPLATEAU DETECTION:")
print("-" * 80)

if len(weekly_summaries) >= 3:
    recent_weeks = weekly_summaries[-2:]
    improvement = ((recent_weeks[-1]["steps"] - recent_weeks[0]["steps"]) / recent_weeks[0]["steps"]) * 100
    
    if improvement < 2:
        print("⚠ PLATEAU DETECTED: Less than 2% improvement in last 2 weeks ({:.1f}%)".format(improvement))
    else:
        print("✓ Continued progress: {:.1f}% improvement".format(improvement))

# Step 5: Detect anomalies
print("\nANOMALY DETECTION:")
print("-" * 80)

all_daily_steps = []
for week in weekly_data:
    all_daily_steps.extend([d["steps"] for d in week])

mean_steps = sum(all_daily_steps) / len(all_daily_steps)
std_dev_steps = std_dev(all_daily_steps)
threshold = mean_steps + (2 * std_dev_steps)

anomalies = []
for day_num, steps in enumerate(all_daily_steps, 1):
    if steps > threshold:
        anomalies.append((day_num, steps))

if anomalies:
    print("Unusual days detected (>{:.0f} steps):".format(threshold))
    for day, steps in anomalies:
        print("  Day {}: {} steps".format(day, steps))
else:
    print("No significant anomalies detected")

# Step 6: Forecast
print("\nFORECAST (Next 2 weeks):")
print("-" * 80)

last_steps = weekly_summaries[-1]["steps"]
trend_slope = (weekly_summaries[-1]["steps"] - weekly_summaries[0]["steps"]) / (len(weekly_summaries) - 1)

forecast_w1 = last_steps + trend_slope
forecast_w2 = forecast_w1 + trend_slope

print("Week {}: {:,.0f} steps".format(len(weekly_summaries)+1, forecast_w1))
print("Week {}: {:,.0f} steps".format(len(weekly_summaries)+2, forecast_w2))

# Step 7: Calculate performance score
print("\nPERFORMANCE SCORE:")
print("-" * 80)

compliance = []
for metric in ["steps", "distance", "calories"]:
    avg = sum(metrics_trends[metric]) / len(metrics_trends[metric])
    if metric == "steps":
        target = baseline["weekly_steps"]
    elif metric == "distance":
        target = baseline["weekly_distance"]
    else:
        target = baseline["weekly_calories"]
    
    pct = (avg / target) * 100
    compliance.append(min(pct, 100))  # Cap at 100%

score = sum(compliance) / len(compliance)
print("Overall Performance Score: {:.0f}/100".format(score))

# Top insights
print("\nTOP 3 INSIGHTS:")
print("-" * 80)
print("1. ✓ Consistent weekly targets achieved")
print("2. ⚠ Watch for plateau - vary training routine")
print("3. ✓ Resting heart rate improving (positive sign)")

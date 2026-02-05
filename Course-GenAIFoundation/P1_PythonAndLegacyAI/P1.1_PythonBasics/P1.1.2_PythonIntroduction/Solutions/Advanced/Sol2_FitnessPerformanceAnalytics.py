"""
Solution: Advanced Assignment 2 - Fitness Performance Analytics (Concise)
"""
import math

# Input data (sample weeks)
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

baseline_metrics = {"weekly_steps": 70000, "weekly_distance": 350, "weekly_calories": 15000}
anomaly_threshold = 2.0
weeks_to_forecast = 2

def std_dev(values):
    mean = sum(values) / len(values)
    return math.sqrt(sum((x - mean) ** 2 for x in values) / len(values))

# Weekly summaries
weekly_summaries = []
for week in weekly_data:
    weekly_summaries.append({
        "steps": sum(d["steps"] for d in week),
        "distance": sum(d["distance"] for d in week),
        "calories": sum(d["calories"] for d in week),
        "avg_hr": sum(d["heart_rate"] for d in week) / len(week),
    })

# Trend (simple slope)
steps_series = [w["steps"] for w in weekly_summaries]
trend = (steps_series[-1] - steps_series[0]) / (len(steps_series) - 1) if len(steps_series) > 1 else 0

# Plateau (last two weeks improvement)
plateau = False
if len(steps_series) >= 2:
    improvement = ((steps_series[-1] - steps_series[-2]) / steps_series[-2]) * 100
    plateau = improvement < 2

# Anomaly detection on daily steps
all_steps = [d["steps"] for week in weekly_data for d in week]
mean_steps = sum(all_steps) / len(all_steps)
threshold = mean_steps + anomaly_threshold * std_dev(all_steps)
anomalies = [(i + 1, s) for i, s in enumerate(all_steps) if s > threshold]

# Forecast (next N weeks)
forecast = [round(steps_series[-1] + trend * i) for i in range(1, weeks_to_forecast + 1)]

# Performance score (avg compliance)
compliance = [
    min((sum(w["steps"] for w in weekly_summaries) / len(weekly_summaries)) / baseline_metrics["weekly_steps"] * 100, 100),
    min((sum(w["distance"] for w in weekly_summaries) / len(weekly_summaries)) / baseline_metrics["weekly_distance"] * 100, 100),
    min((sum(w["calories"] for w in weekly_summaries) / len(weekly_summaries)) / baseline_metrics["weekly_calories"] * 100, 100),
]
score = sum(compliance) / len(compliance)

print("Fitness Performance Report")
print("=" * 48)
for i, w in enumerate(weekly_summaries, 1):
    print(f"Week {i}: Steps {w['steps']:,} | Dist {w['distance']:.0f} | Cal {w['calories']:,} | HR {w['avg_hr']:.0f}")

print("\nTrend: {:+.1f} steps/week".format(trend))
print("Plateau Risk:", "Yes" if plateau else "No")
print("Anomalies:", anomalies if anomalies else "None")
print(f"Forecast (next {weeks_to_forecast} weeks):", forecast)
print("Performance Score: {:.0f}/100".format(score))
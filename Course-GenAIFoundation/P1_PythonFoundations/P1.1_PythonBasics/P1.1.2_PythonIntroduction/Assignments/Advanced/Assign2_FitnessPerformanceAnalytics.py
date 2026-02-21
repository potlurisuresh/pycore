"""
Advanced Assignment 2: Fitness Performance Analytics

Scenario:
Analyze multi‑week fitness data to summarize performance, detect anomalies and
plateaus, forecast trends, and produce insights.

Inputs:
- weekly_data (list of weeks; each day has steps, distance, calories, heart_rate)
- baseline_metrics (weekly targets)
- anomaly_threshold (std‑dev multiplier)
- weeks_to_forecast (int)

Tasks:
1) Compute weekly totals/averages per metric.
2) Compare against baselines and compute variance %.
3) Detect trend direction and plateau risk.
4) Flag anomalies using mean/std‑dev.
5) Forecast next N weeks and compute a score.

Output (sample):
- Weekly summaries + trend
- Anomaly list + plateau flag
- Forecast + performance score + top insights

Hints:
- Trend = (last - first) / (n-1)
- Anomaly if value > mean + k*std

Rubric:
- Aggregation, variance, anomaly, trend/forecast, report clarity
"""

"""
Advanced Assignment 1: Budget Optimization Engine

Scenario:
Analyze multi‑month spending to find overspending, forecast next months, and
recommend savings actions.

Inputs:
- spending_history (dict: month -> category -> amount)
- budget_targets (dict: category -> target)
- inflation_rate (float)
- months_to_forecast (int)

Tasks:
1) Aggregate category totals and averages.
2) Compute variance vs targets and savings opportunities.
3) Estimate trends and forecast future spending.
4) Calculate a health score (0–100).
5) Output top 3 recommendations.

Output (sample):
- Category variances and savings potential
- Forecast for next N months
- Health score + recommendations

Hints:
- Variance % = (avg - target) / target * 100
- Trend = (last - first) / (n-1)

Rubric:
- Aggregation, variance, forecasting, score, report clarity
"""

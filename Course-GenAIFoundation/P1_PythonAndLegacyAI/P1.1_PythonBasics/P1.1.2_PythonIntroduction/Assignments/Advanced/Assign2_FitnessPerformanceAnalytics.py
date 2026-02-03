"""
Advanced Assignment 2: Fitness Performance Analytics

Scenario:
A health platform analyzes multi-week fitness data to track performance, identify
training patterns, detect plateaus, predict future performance, and generate personalized
training insights.

Objective:
Analyze comprehensive fitness data (steps, distance, calories, heart rate) across
multiple weeks to calculate metrics, identify patterns, detect anomalies, forecast
performance, and provide actionable insights.

Inputs:
- weekly_data (list of weeks, each week has daily metrics dict)
  Each day: {"steps": int, "distance": float, "calories": int, "heart_rate": int}
- baseline_metrics (dict with weekly targets for each metric)
- anomaly_threshold (float, standard deviations for anomaly detection)
- weeks_to_forecast (integer)

Outputs:
- Weekly summaries (totals, averages, max values)
- Performance vs baseline (variance analysis)
- Trend analysis (improvement/decline per metric)
- Anomalies detected (unusual days)
- Plateau detection (no improvement for N weeks)
- Forecast for next N weeks
- Performance score (0-100)
- Top 3 insights and recommendations

Steps / Logic Checklist:
1) Parse nested weekly data structure.
2) Calculate weekly totals and averages for each metric.
3) Compare to baseline targets (variance %).
4) Calculate trend line per metric (linear progression).
5) Identify plateau weeks (< 2% improvement for N consecutive weeks).
6) Detect anomalies (days > 2 std devs from weekly mean).
7) Calculate composite performance score.
8) Generate forecast using trend + seasonal adjustment.
9) Identify top 3 insights (biggest gaps, best progress, risk areas).
10) Format professional analytics report.

Constraints:
- At least 4 weeks of data (28+ days).
- Each day has all 4 metrics (steps, distance, calories, heart_rate).
- Baseline targets are realistic positive numbers.
- Anomaly threshold > 0 (typically 1.5-2.0).

Example:
Input: (4 weeks of daily data with all metrics)
baseline: {"weekly_steps": 70000, "weekly_distance": 350, "weekly_calories": 15000, "hr_resting": 60}

Output:
Weekly Performance:
Week 1: Steps 68000 (97%), Distance 340km (97%), Calories 14500 (97%), Avg HR 72
Week 2: Steps 71000 (101%), Distance 355km (101%), Calories 15200 (101%), Avg HR 70
Week 3: Steps 70500 (101%), Distance 352km (101%), Calories 15100 (101%), Avg HR 71
Week 4: Steps 70000 (100%), Distance 348km (99%), Calories 15000 (100%), Avg HR 72
Trends: Steps (↗ improving), Distance (↗ stable), Calories (↗ stable), HR (↘ resting improving)
Anomalies: Week 2 Day 5 (unusual spike)
Plateau Risk: Detected - no progress last 2 weeks
Forecast W5-6: Steps 70500, Distance 350km
Score: 82/100
Top Insights:
1. Excellent distance performance (101% avg)
2. Resting heart rate improving (positive trend)
3. Watch for training plateau - vary routine

Hints:
- Use list comprehension for aggregating daily metrics.
- Calculate mean and std dev for anomaly detection.
- Trend: use linear regression concept or simple slope calculation.
- Performance score: weighted average of compliance %s.
- Forecast: extend trend line + adjust for recent variance.

Rubric:
- Parsing multi-level weekly data: 10%
- Weekly aggregations (totals, averages): 10%
- Baseline comparison and variance: 12%
- Trend analysis and calculation: 12%
- Plateau detection logic: 12%
- Anomaly detection (statistical): 12%
- Forecast generation: 12%
- Performance score calculation: 10%
- Insight generation and ranking: 10%

"""

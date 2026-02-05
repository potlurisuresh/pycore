"""
Advanced Assignment 5: Climate Pattern Recognition and Prediction

Scenario:
Analyze temperature time‑series to detect anomalies, heat/cold events, and
forecast near‑term trends with alerts.

Inputs:
- temperature_data (date, temp_min, temp_max, humidity, pressure)
- seasonal_baselines, alert_thresholds
- analysis_window, forecast_days

Tasks:
1) Compute rolling averages and anomaly scores.
2) Detect heat waves/cold snaps (consecutive days beyond threshold).
3) Analyze pressure trend and generate forecast.
4) Produce a risk score and concise alerts.

Output:
- Anomaly flags, event detection, forecast, alerts, risk score.

Hints:
- Anomaly = (value - seasonal_avg) / seasonal_std
- Heat wave: >= 3 consecutive days above threshold.

Rubric:
- Anomaly detection, event logic, forecast, alert quality.
"""

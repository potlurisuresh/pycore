"""
Solution: Advanced Assignment 5 - Climate Pattern Prediction (Concise)
"""
import math

# Generate sample data (120 days)
def generate_sample_data(days=120):
    data = []
    base = 20
    for day in range(days):
        if day < 45:
            max_temp = base + day * 0.2
        elif day < 75:
            max_temp = base + 10 + (day % 10) * 0.5
        else:
            max_temp = base + (22 if 75 <= day <= 82 else 12 + (120 - day) * 0.1)
        min_temp = max_temp - 8
        avg_temp = (min_temp + max_temp) / 2
        data.append({
            "day": day + 1,
            "avg": avg_temp,
            "pressure": 1010 + math.sin(day / 20) * 5,
        })
    return data

temperature_data = generate_sample_data()
heat_threshold = 35
cold_threshold = 0
rolling_window = 7
forecast_days = 7

def std_dev(values):
    mean = sum(values) / len(values)
    return math.sqrt(sum((x - mean) ** 2 for x in values) / len(values))

temps = [d["avg"] for d in temperature_data]
pressures = [d["pressure"] for d in temperature_data]

baseline = sum(temps[:30]) / 30
baseline_std = std_dev(temps[:30])

rolling_avgs = []
for i in range(len(temps)):
    window = temps[max(0, i - rolling_window + 1): i + 1]
    rolling_avgs.append(sum(window) / len(window))

anomalies = [
    (i + 1, t)
    for i, t in enumerate(temps)
    if abs((t - baseline) / baseline_std) > 2
]

# Heat wave detection
heat_waves = []
start = None
for i, t in enumerate(temps):
    if t >= heat_threshold:
        start = i if start is None else start
    else:
        if start is not None and i - start >= 3:
            heat_waves.append((start + 1, i))
        start = None
if start is not None and len(temps) - start >= 3:
    heat_waves.append((start + 1, len(temps)))

# Pressure trend
mid = len(pressures) // 2
pressure_trend = (sum(pressures[mid:]) / (len(pressures) - mid)) - (sum(pressures[:mid]) / mid)

# Forecast (simple trend)
trend = (temps[-1] - temps[-rolling_window]) / rolling_window
forecast = [round(temps[-1] + trend * i, 1) for i in range(1, forecast_days + 1)]

# Risk score
risk = min(100, len(anomalies) * 2 + len(heat_waves) * 20 + (20 if abs(pressure_trend) > 5 else 0))

print("Climate Pattern Report")
print("=" * 48)
print(f"Baseline: {baseline:.1f}°C (±{baseline_std:.1f})")
print(f"Anomalies: {len(anomalies)}")
print(f"Heat Waves: {heat_waves if heat_waves else 'None'}")
print(f"Pressure Trend: {pressure_trend:.1f} hPa")
print(f"Forecast (next {forecast_days} days): {forecast}")
print(f"Risk Score: {risk}/100")

print("\nAlerts:")
if heat_waves:
    print("- Heat wave conditions detected")
if anomalies:
    print("- Temperature anomalies detected")
if abs(pressure_trend) > 5:
    print("- Significant pressure shift")
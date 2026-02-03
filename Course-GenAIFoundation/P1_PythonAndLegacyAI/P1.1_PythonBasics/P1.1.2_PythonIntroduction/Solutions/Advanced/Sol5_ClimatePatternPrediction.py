"""
Solution: Advanced Assignment 5 - Climate Pattern Recognition and Prediction

This solution demonstrates:
- Rolling average calculation
- Anomaly detection using standard deviation
- Heat wave and cold snap detection
- Pressure trend analysis
- Forecasting with trend projection
- Risk scoring and alert generation
"""

import math

# Input data: 120 days of temperature readings
temperature_data = [
    {"date": "Apr01", "temp_min": 18, "temp_max": 24, "humidity": 65, "pressure": 1010},
    {"date": "Apr02", "temp_min": 19, "temp_max": 25, "humidity": 68, "pressure": 1012},
    {"date": "Apr03", "temp_min": 17, "temp_max": 23, "humidity": 62, "pressure": 1015},
    # ... (120 days total, showing subset)
    # Simulating 90 days with normal temps + 30 days with heat wave
]

# Generate realistic data for demonstration
def generate_sample_data():
    data = []
    base_temp = 20
    for day in range(120):
        if day < 45:  # Spring: gradual warming
            max_temp = base_temp + (day * 0.2) + (5 if day % 3 == 0 else 0)
            min_temp = max_temp - 8
        elif day < 75:  # Early summer: heat wave approaching
            max_temp = base_temp + 10 + (day % 10) * 0.5
            min_temp = max_temp - 8
        else:  # Mid-summer: heat wave (days 75-82)
            if 75 <= day <= 82:
                max_temp = base_temp + 22  # 42°C peak
                min_temp = max_temp - 6
            else:
                max_temp = base_temp + 12 + (120 - day) * 0.1
                min_temp = max_temp - 8
        
        avg_temp = (min_temp + max_temp) / 2
        humidity = 60 + (day % 20)
        pressure = 1010 + math.sin(day / 20) * 5
        
        data.append({
            "day": day + 1,
            "min": min_temp,
            "max": max_temp,
            "avg": avg_temp,
            "humidity": humidity,
            "pressure": pressure,
        })
    return data

temperature_data = generate_sample_data()

# Configuration
heat_threshold = 35
cold_threshold = 0
consecutive_threshold = 3
rolling_window = 7
forecast_days = 7

# Helper function: calculate standard deviation
def std_dev(values):
    if len(values) == 0:
        return 0
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return math.sqrt(variance)

# Step 1: Extract temperatures
temps = [d["avg"] for d in temperature_data]
pressures = [d["pressure"] for d in temperature_data]

# Step 2: Calculate seasonal baseline (first month = April)
seasonal_baseline = sum(temps[:30]) / 30
seasonal_std = std_dev(temps[:30])

print("CLIMATE ANALYSIS REPORT")
print("=" * 80)
print("Data Period: Days 1-{}".format(len(temperature_data)))
print("Seasonal Baseline: {:.1f}°C (±{:.1f}°C)".format(seasonal_baseline, seasonal_std))
print("=" * 80)

# Step 3: Calculate rolling averages
rolling_avgs = []
for i in range(len(temps)):
    window = temps[max(0, i - rolling_window + 1):i + 1]
    rolling_avgs.append(sum(window) / len(window))

# Step 4: Detect daily anomalies
print("\nDAILY ANOMALY DETECTION:")
print("-" * 80)

anomalies = []
for i, temp in enumerate(temps):
    z_score = (temp - seasonal_baseline) / seasonal_std if seasonal_std > 0 else 0
    
    if abs(z_score) > 2:
        anomaly_type = "EXTREME" if abs(z_score) > 3 else "UNUSUAL"
        anomalies.append((i + 1, temp, z_score, anomaly_type))

if anomalies:
    print("Found {} anomalies:".format(len(anomalies)))
    for day, temp, z_score, atype in anomalies[:10]:  # Show first 10
        print("  Day {}: {:.1f}°C (z-score: {:.2f}) - {}".format(day, temp, z_score, atype))
else:
    print("No significant anomalies detected")

# Step 5: Detect heat waves
print("\nHEAT WAVE DETECTION:")
print("-" * 80)

heat_wave_start = None
heat_wave_length = 0
heat_waves = []
heat_wave_temps = []

for i, temp in enumerate(temps):
    if temp >= heat_threshold:
        if heat_wave_start is None:
            heat_wave_start = i
            heat_wave_temps = [temp]
        else:
            heat_wave_temps.append(temp)
        heat_wave_length += 1
    else:
        if heat_wave_length >= consecutive_threshold:
            heat_waves.append({
                "start": heat_wave_start + 1,
                "end": heat_wave_start + heat_wave_length,
                "length": heat_wave_length,
                "peak": max(heat_wave_temps),
                "avg": sum(heat_wave_temps) / len(heat_wave_temps),
            })
        heat_wave_start = None
        heat_wave_length = 0
        heat_wave_temps = []

# Check last sequence
if heat_wave_length >= consecutive_threshold:
    heat_waves.append({
        "start": heat_wave_start + 1,
        "end": heat_wave_start + heat_wave_length,
        "length": heat_wave_length,
        "peak": max(heat_wave_temps),
        "avg": sum(heat_wave_temps) / len(heat_wave_temps),
    })

if heat_waves:
    for hw in heat_waves:
        print("Heat Wave: Days {}-{} ({} consecutive days)".format(hw['start'], hw['end'], hw['length']))
        print("  Peak: {:.1f}°C, Average: {:.1f}°C".format(hw['peak'], hw['avg']))
else:
    print("No heat waves detected")

# Step 6: Detect cold snaps
print("\nCOLD SNAP DETECTION:")
print("-" * 80)

cold_snaps = []
cold_start = None
cold_length = 0
cold_temps = []

for i, temp in enumerate(temps):
    if temp <= cold_threshold:
        if cold_start is None:
            cold_start = i
            cold_temps = [temp]
        else:
            cold_temps.append(temp)
        cold_length += 1
    else:
        if cold_length >= consecutive_threshold:
            cold_snaps.append({
                "start": cold_start + 1,
                "end": cold_start + cold_length,
                "length": cold_length,
            })
        cold_start = None
        cold_length = 0
        cold_temps = []

if cold_snaps:
    for cs in cold_snaps:
        print("Cold Snap: Days {}-{} ({} consecutive days)".format(cs['start'], cs['end'], cs['length']))
else:
    print("No cold snaps detected")

# Step 7: Pressure trend analysis
print("\nPRESSURE TREND ANALYSIS:")
print("-" * 80)

first_half_pressure = sum(pressures[:len(pressures)//2]) / (len(pressures)//2)
second_half_pressure = sum(pressures[len(pressures)//2:]) / (len(pressures) - len(pressures)//2)
pressure_trend = second_half_pressure - first_half_pressure

if pressure_trend > 2:
    pressure_status = "Rising (improving weather expected)"
elif pressure_trend < -2:
    pressure_status = "Falling (unstable weather possible)"
else:
    pressure_status = "Stable"

print("Average: {:.1f} hPa".format(sum(pressures)/len(pressures)))
print("Trend: {}".format(pressure_status))

# Step 8: Forecast
print("\nFORECAST (Next {} days):".format(forecast_days))
print("-" * 80)

# Simple trend-based forecast
last_temp = temps[-1]
trend = (temps[-1] - temps[-rolling_window]) / rolling_window if rolling_window <= len(temps) else 0

for day in range(1, forecast_days + 1):
    forecast_temp = last_temp + (trend * day)
    print("Day {}: {:.1f}°C".format(len(temps) + day, forecast_temp))

# Step 9: Calculate risk score
print("\nCLIMATE RISK SCORE:")
print("-" * 80)

risk_score = 0

# Heat wave risk
if heat_waves:
    risk_score += 30
    risk_score += len(heat_waves) * 10

# Anomalies
risk_score += len(anomalies) * 2

# Pressure instability
if abs(pressure_trend) > 5:
    risk_score += 20

# Cold snap risk (less common in summer)
if cold_snaps:
    risk_score += 15

risk_score = min(risk_score, 100)  # Cap at 100

print("Risk Score: {}/100".format(risk_score))
if risk_score > 75:
    print("Status: EXTREME RISK")
elif risk_score > 50:
    print("Status: HIGH RISK")
elif risk_score > 25:
    print("Status: MODERATE RISK")
else:
    print("Status: LOW RISK")

# Step 10: Alerts and recommendations
print("\nALERTS AND RECOMMENDATIONS:")
print("-" * 80)

if heat_waves:
    print("⚠️  HEAT ALERT: Dangerous conditions expected")
    print("   - Stay hydrated, avoid peak hours (11 AM - 4 PM)")
    print("   - Watch for heat-related health risks")
    print("   - Increase air conditioning demand")

if anomalies:
    print("⚠️  WEATHER ANOMALY: Unusual temperatures detected")
    print("   - Plan accordingly for rapid weather changes")

if abs(pressure_trend) > 5:
    print("⚠️  PRESSURE CHANGE: Significant pressure shift")
    print("   - Monitor for severe weather development")

print("\n" + "=" * 80)

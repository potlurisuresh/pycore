"""
Solution: Intermediate Assignment 5 - Temperature Trend Analyzer (Concise)
"""

# Input data
daily_temps = [28, 31, 33, 35, 32, 29, 30, 28, 27, 32]
hot_threshold = 30
consecutive_days = 3

# Step 1-3: Parse and find extremes, calculate average
highest_temp = max(daily_temps)
lowest_temp = min(daily_temps)
avg_temp = sum(daily_temps) / len(daily_temps)

print("Temperature Analysis")
print("=" * 50)
print("Highest: {}°C".format(highest_temp))
print("Lowest: {}°C".format(lowest_temp))
print("Average: {:.1f}°C".format(avg_temp))

# Step 4: Count hot days
hot_day_count = sum(1 for temp in daily_temps if temp >= hot_threshold)
print("Hot Days (>= {}°C): {}".format(hot_threshold, hot_day_count))

# Step 5: Identify consecutive hot days (heat wave)
print("\nHeat Wave Detection ({}+ consecutive days):".format(consecutive_days))

heat_wave_start = None
heat_wave_length = 0
heat_waves = []

for i, temp in enumerate(daily_temps):
    if temp >= hot_threshold:
        if heat_wave_start is None:
            heat_wave_start = i
        heat_wave_length += 1
    else:
        if heat_wave_length >= consecutive_days:
            heat_waves.append({
                "start": heat_wave_start + 1,  # Day 1-indexed
                "end": heat_wave_start + heat_wave_length,
                "length": heat_wave_length
            })
        heat_wave_start = None
        heat_wave_length = 0

# Check if last sequence was a heat wave
if heat_wave_length >= consecutive_days:
    heat_waves.append({
        "start": heat_wave_start + 1,
        "end": heat_wave_start + heat_wave_length,
        "length": heat_wave_length
    })

if heat_waves:
    for hw in heat_waves:
        print("  Days {}-{} ({} consecutive days)".format(hw['start'], hw['end'], hw['length']))
else:
    print("  No heat waves detected")

# Step 6: Calculate daily temperature changes
print("\nDaily Temperature Changes (>|2°C|):")
for i in range(1, len(daily_temps)):
    change = daily_temps[i] - daily_temps[i - 1]
    if abs(change) > 2:
        print("  Day {} → {}: {:.1f}°C".format(i, i + 1, change))

# Step 7-8: Determine trend
first_half_avg = sum(daily_temps[:len(daily_temps)//2]) / (len(daily_temps)//2)
second_half_avg = sum(daily_temps[len(daily_temps)//2:]) / (len(daily_temps) - len(daily_temps)//2)

trend_diff = second_half_avg - first_half_avg
if trend_diff > 1:
    trend = "Warming trend"
elif trend_diff < -1:
    trend = "Cooling trend"
else:
    trend = "Stable"

print("\nTrend Analysis:")
print("  First half avg: {:.1f}°C".format(first_half_avg))
print("  Second half avg: {:.1f}°C".format(second_half_avg))
print("  Overall: {}".format(trend))

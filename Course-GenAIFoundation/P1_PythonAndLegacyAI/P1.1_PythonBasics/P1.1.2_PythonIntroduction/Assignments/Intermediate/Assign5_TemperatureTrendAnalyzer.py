"""
Intermediate Assignment 5: Temperature Trend Analyzer

Scenario:
A weather monitoring system tracks daily temperatures over time and needs to identify
temperature trends, find consecutive hot days, and calculate trend metrics.

Objective:
Analyze temperature data to find temperature trends, identify consecutive hot days,
calculate daily changes, and determine if temperature is rising or falling.

Inputs:
- daily_temps (list of floats, temperature readings)
- hot_threshold (float, temperature considered hot)
- consecutive_days (integer, minimum consecutive days for a "heat wave")

Outputs:
- Highest and lowest temperatures
- Hot day count and heat wave detection
- Average temperature
- Temperature trend (rising/falling/stable)
- Days with significant temperature changes (>5°C)

Steps / Logic Checklist:
1) Parse the temperature list.
2) Find highest and lowest temperatures.
3) Calculate average temperature.
4) Count total hot days (>= hot_threshold).
5) Identify consecutive hot days (heat wave).
6) Calculate daily temperature changes (day[i] - day[i-1]).
7) Find days with significant changes (>5°C).
8) Determine overall trend (compare start vs end average).
9) Print comprehensive report.

Constraints:
- At least 3 days of temperature data.
- All temperatures are valid floats.
- hot_threshold is a positive number.

Example:
Input: daily_temps=[28, 31, 33, 35, 32, 29, 30, 28, 27, 32],
       hot_threshold=30,
       consecutive_days=3
Output:
Highest: 35°C, Lowest: 27°C, Average: 30.5°C
Hot Days: 6
Heat Wave: Days 1-3 (3 consecutive days)
Significant Changes: Day 4→5 (-3°C), Day 6→7 (+1°C)
Trend: Stable (slight cooling trend)

Hints:
- Use max() and min() for extremes.
- Use loops with index to compare consecutive days.
- Track consecutive hot days with a counter.
- Calculate differences: next_day - current_day
- Compare first half avg vs second half avg for trend.

Rubric:
- Finding min/max temperatures: 15%
- Calculating average: 10%
- Counting hot days: 15%
- Detecting consecutive hot days/heat waves: 20%
- Calculating daily changes: 15%
- Identifying significant changes: 15%
- Determining overall trend: 10%

"""

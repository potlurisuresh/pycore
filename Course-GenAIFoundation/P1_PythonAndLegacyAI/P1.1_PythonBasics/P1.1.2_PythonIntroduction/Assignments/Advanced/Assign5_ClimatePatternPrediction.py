"""
Advanced Assignment 5: Climate Pattern Recognition and Prediction

Scenario:
A meteorological system monitors temperature patterns to detect climate anomalies,
identify seasonal trends, predict future weather patterns, and generate weather alerts
based on multiple factors.

Objective:
Analyze comprehensive temperature data across multiple months to detect patterns,
identify anomalies, forecast trends, calculate climate indices, and generate
predictive alerts for unusual weather.

Inputs:
- temperature_data (list of dicts: {date, temp_min, temp_max, humidity, pressure})
- seasonal_baselines (dict: {season: avg_temp_range})
- alert_thresholds (dict: {heat_wave, cold_snap, pressure_drop, etc})
- analysis_window (integer, days for rolling average)
- forecast_days (integer, days to predict ahead)

Outputs:
- Daily anomaly flags (normal/unusual/extreme)
- Heat wave detection (duration, severity)
- Cold snap detection (duration, severity)
- Seasonal deviation analysis
- Pressure trend analysis
- Rolling average trends
- Forecast for next N days
- Alert summary (count and types)
- Climate risk score (0-100)
- Actionable weather recommendations

Steps / Logic Checklist:
1) Parse daily temperature data (min, max, humidity, pressure).
2) Calculate rolling averages (N-day smoothing).
3) Identify baseline values per season.
4) Calculate daily anomaly score (deviation from seasonal baseline).
5) Flag anomalies: normal (<1σ), unusual (1-2σ), extreme (>2σ).
6) Detect heat waves: consecutive days > threshold with severity calculation.
7) Detect cold snaps: consecutive days < threshold with severity calculation.
8) Analyze pressure trends (rising/falling/stable).
9) Detect correlation between pressure drops and temperature changes.
10) Calculate climate risk score (sum of all risk factors).
11) Generate forecast using trend + seasonal adjustment.
12) Generate contextual alerts and recommendations.
13) Format comprehensive climate report.

Constraints:
- Minimum 90 days of data for seasonal analysis.
- All temperature values in Celsius (reasonable range: -40 to +50).
- Humidity 0-100%, Pressure in hPa (900-1050 typical).
- Alert thresholds customizable per region.

Example:
Input: 120 days of data (Apr-Jul in northern hemisphere)
Heat threshold: 35°C, Cold threshold: 0°C
Rolling window: 7 days

Output:
DAILY ANALYSIS (Sample):
Day 1: 22°C, Normal (within 1σ)
Day 45: 38°C, EXTREME anomaly (>2σ above seasonal avg)
Day 46: 39°C, EXTREME anomaly (>2σ above seasonal avg)
...

HEAT WAVE DETECTION:
Heat Wave #1: Days 45-51 (7 consecutive days >35°C)
Duration: 7 days
Severity: Extreme (peak 42°C, avg 38.5°C)
Impact: Dangerous heat conditions

COLD SNAP DETECTION:
None detected in this period

SEASONAL ANALYSIS:
Season: Spring transitioning to Summer
Expected: 20-28°C
Actual average: 26°C (within normal range)
Deviation: -1.5% (slightly cooler than historical avg)

PRESSURE TRENDS:
Pressure average: 1010 hPa (stable)
Trend: Minor fluctuation, no significant patterns
Correlation: Pressure drops → small temp dip (weak correlation)

ROLLING 7-DAY AVERAGES:
Week 1: 23°C, Week 2: 24°C, Week 3: 26°C, ..., Week 17: 27°C
Trend: Warming trend over period (↗)

FORECAST (Next 7 days):
Day 121: 28°C (slight warm)
Day 122: 29°C (warm trend continuing)
...
Day 127: 31°C (approaching threshold)

CLIMATE RISK SCORE: 65/100
(Moderate risk due to heat wave event)

ALERTS GENERATED:
- Heat Wave Alert (Days 45-51)
- Extreme Heat Warning (Days 46-49)
- Humidity High (Days 45-51)

RECOMMENDATIONS:
1. Heat safety: Stay hydrated, avoid peak hours (11 AM - 4 PM)
2. Infrastructure: Watch for heat damage, increased cooling demand
3. Health: Vulnerable populations at risk - proactive outreach
4. Agriculture: Irrigation needs increase significantly
5. Forecast next 5 days - pressure changes may bring relief

Hints:
- Use rolling mean formula: avg of last N values.
- Standard deviation: calculate for seasonal data.
- Anomaly score: (value - seasonal_avg) / seasonal_std
- Heat wave: consecutive days > threshold (at least 3 for definition).
- Forecast: extend trend line + adjust for seasonal pattern + recent volatility.
- Risk score: weight anomalies (extreme=3, unusual=1) + heat/cold duration.

Rubric:
- Parsing temperature and metadata: 10%
- Rolling average calculation: 10%
- Seasonal baseline and anomaly detection: 12%
- Heat wave and cold snap identification: 12%
- Pressure trend analysis: 10%
- Correlation analysis (pressure-temp): 10%
- Climate risk score calculation: 10%
- Forecast generation: 12%
- Alert generation and recommendations: 12%

"""

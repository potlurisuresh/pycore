"""
Solution: Advanced Assignment 1 - Budget Optimization Engine

This solution demonstrates:
- Multi-level nested dictionary handling
- Variance analysis and calculations
- Forecasting with trend projection
- Ranking and filtering operations
- Comprehensive reporting
"""

# Input data
spending_history = {
    "January": {"food": 300, "transport": 120, "utilities": 80},
    "February": {"food": 320, "transport": 115, "utilities": 85},
    "March": {"food": 340, "transport": 130, "utilities": 80},
}

budget_targets = {"food": 280, "transport": 100, "utilities": 100}
inflation_rate = 0.05
months_to_forecast = 2

# Step 1-2: Aggregate spending by category across months
category_totals = {}
for month, categories in spending_history.items():
    for category, amount in categories.items():
        if category not in category_totals:
            category_totals[category] = []
        category_totals[category].append(amount)

# Calculate averages and variance
print("CATEGORY ANALYSIS:")
print("-" * 70)

analysis = {}
total_overspending = 0

for category, amounts in category_totals.items():
    avg_spending = sum(amounts) / len(amounts)
    target = budget_targets[category]
    variance = ((avg_spending - target) / target) * 100
    overspending = max(0, avg_spending - target)
    
    analysis[category] = {
        "avg": avg_spending,
        "target": target,
        "variance": variance,
        "opportunity": overspending * len(spending_history)  # Total savings if brought to target
    }
    
    status = "OVER" if variance > 0 else "OK"
    print("{:12s}: Avg ${:6.2f} | Target ${:6.2f} | {} {:+.1f}%".format(category, avg_spending, target, status, variance))
    
    if variance > 0:
        total_overspending += analysis[category]["opportunity"]

# Step 3: Calculate trends (month-over-month growth)
print("\nMONTH-OVER-MONTH TRENDS:")
print("-" * 70)

trends = {}
for category, amounts in category_totals.items():
    if len(amounts) > 1:
        growth_rate = ((amounts[-1] - amounts[0]) / amounts[0]) * 100 / (len(amounts) - 1)
        trends[category] = growth_rate
        direction = "↗" if growth_rate > 0 else "↘"
        print("{:12s}: {:+.2f}% per month {}".format(category, growth_rate, direction))

# Step 4: Forecast future spending
print("\nFORECAST (Next {} months):".format(months_to_forecast))
print("-" * 70)

forecasts = {}
for category, amounts in category_totals.items():
    last_amount = amounts[-1]
    growth = trends.get(category, 0)
    
    forecast_values = []
    for month in range(1, months_to_forecast + 1):
        inflated = last_amount * ((1 + inflation_rate) ** month)
        growth_adjustment = inflated * ((1 + growth/100) ** month)
        forecast_values.append(growth_adjustment)
    
    forecasts[category] = forecast_values
    print("{:12s}: {}".format(category, ["${:.0f}".format(v) for v in forecast_values]))

# Step 5: Calculate health score
compliance_scores = []
for category, data in analysis.items():
    if data["variance"] <= 0:
        score = 100
    elif data["variance"] <= 10:
        score = 90
    elif data["variance"] <= 20:
        score = 75
    else:
        score = 50
    compliance_scores.append(score)

health_score = sum(compliance_scores) / len(compliance_scores)

# Step 6: Generate recommendations
print("\nOPTIMIZATION RECOMMENDATIONS:")
print("-" * 70)

recommendations = []
for category, data in analysis.items():
    if data["opportunity"] > 0:
        monthly_savings = data["opportunity"] / len(spending_history)
        recommendations.append({
            "category": category,
            "savings": data["opportunity"],
            "monthly": monthly_savings,
            "variance": data["variance"]
        })

# Sort by savings potential
recommendations.sort(key=lambda x: x["savings"], reverse=True)

for i, rec in enumerate(recommendations[:3], 1):
    print("{}. {}: Reduce by ${:.2f}/month".format(i, rec['category'].capitalize(), rec['monthly']))
    print("   → Saves ${:.2f}/period ({:.1f}% over)".format(rec['savings'], rec['variance']))

# Final summary
print("\n" + "=" * 70)
print("Budget Health Score: {:.0f}/100".format(health_score))
print("Total Savings Potential: ${:.2f}".format(total_overspending))
print("=" * 70)

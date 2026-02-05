"""
Solution: Advanced Assignment 1 - Budget Optimization Engine (Concise)
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

# Aggregate by category
category_totals = {c: [] for c in budget_targets}
for _, categories in spending_history.items():
    for category, amount in categories.items():
        category_totals[category].append(amount)

analysis = {}
for category, amounts in category_totals.items():
    avg_spend = sum(amounts) / len(amounts)
    target = budget_targets[category]
    variance = ((avg_spend - target) / target) * 100
    opportunity = max(0, avg_spend - target) * len(spending_history)
    analysis[category] = {
        "avg": avg_spend,
        "target": target,
        "variance": variance,
        "opportunity": opportunity,
    }

# Trend and forecast
trends = {}
forecasts = {}
for category, amounts in category_totals.items():
    slope = (amounts[-1] - amounts[0]) / (len(amounts) - 1)
    trends[category] = slope

    last = amounts[-1]
    forecasts[category] = [
        round(last * ((1 + inflation_rate) ** m) + slope * m, 2)
        for m in range(1, months_to_forecast + 1)
    ]

# Health score (simple compliance)
scores = []
for data in analysis.values():
    if data["variance"] <= 0:
        scores.append(100)
    elif data["variance"] <= 10:
        scores.append(90)
    elif data["variance"] <= 20:
        scores.append(75)
    else:
        scores.append(50)

health_score = sum(scores) / len(scores)

# Recommendations
recommendations = [
    (cat, data["opportunity"], data["variance"])
    for cat, data in analysis.items()
    if data["opportunity"] > 0
]
recommendations.sort(key=lambda x: x[1], reverse=True)

print("Budget Optimization Report")
print("=" * 48)
for category, data in analysis.items():
    status = "OVER" if data["variance"] > 0 else "OK"
    print(
        f"{category:10s} Avg ${data['avg']:.2f} | Target ${data['target']:.2f} | {status} {data['variance']:+.1f}%"
    )

print("\nForecast (Next {} months):".format(months_to_forecast))
for category, values in forecasts.items():
    print(f"{category:10s}: {values}")

print("\nHealth Score: {:.0f}/100".format(health_score))
print("Recommendations:")
for i, (cat, savings, var) in enumerate(recommendations[:3], 1):
    monthly = savings / len(spending_history)
    print(f"{i}. Reduce {cat} by ${monthly:.2f}/month ({var:.1f}% over)")
"""
Advanced Assignment 1: Budget Optimization Engine

Scenario:
A personal finance platform helps users optimize spending across multiple categories
over multiple months. The system must identify overspending patterns, calculate savings
potential, and suggest budget adjustments based on historical data and targets.

Objective:
Analyze multi-month spending data, detect category overspending, calculate savings
opportunities, forecast future spending, and generate optimization recommendations.

Inputs:
- spending_history (dict of months → categories → amounts)
- budget_targets (dict of categories → target amounts)
- inflation_rate (float, monthly rate)
- months_to_forecast (integer)

Outputs:
- Category analysis (actual vs target)
- Over/under spending per category across months
- Savings opportunity per category (cumulative)
- Forecast for next N months
- Top 3 recommendations for savings
- Overall budget health score (0-100)

Steps / Logic Checklist:
1) Parse multi-level nested dictionary structure.
2) Calculate total per category across all months (aggregation).
3) Compare category totals to budget targets (variance analysis).
4) Identify categories exceeding targets by X% (overspending threshold).
5) Calculate potential savings if brought to target (opportunity).
6) Compute month-over-month growth rate per category.
7) Project future spending using growth rate and inflation (forecast).
8) Calculate overall budget health score based on target compliance.
9) Generate prioritized recommendations (top savings opportunities).
10) Format comprehensive analysis report.

Constraints:
- At least 3 months of historical data.
- At least 3 spending categories.
- All values are positive numbers.
- Budget targets should be realistic (not zero).
- Inflation rate between 0 and 0.5 (0-50%).

Example:
Input: spending_history = {
    "Jan": {"food": 300, "transport": 120, "utilities": 80},
    "Feb": {"food": 320, "transport": 115, "utilities": 85},
    "Mar": {"food": 340, "transport": 130, "utilities": 80}
}
budget_targets = {"food": 280, "transport": 100, "utilities": 100}
inflation_rate = 0.05, months_to_forecast = 2

Output:
Category Analysis:
- food: Avg 320/month, Target 280 (OVER by 14%)
- transport: Avg 122/month, Target 100 (OVER by 22%)
- utilities: Avg 82/month, Target 100 (OK)
Savings Potential: food=$120, transport=$66
Forecast (Apr-May): food=[357,375], transport=[136,143]
Health Score: 65/100
Top Recommendations:
1. Reduce food spending by $40/month (saves $480/year)
2. Reduce transport by $22/month (saves $264/year)

Hints:
- Use nested loops for aggregating categories across months.
- Calculate variance: (actual - target) / target * 100
- Compute month-over-month growth: (current - previous) / previous
- Use list comprehension for sorting and filtering recommendations.
- Health score: sum of compliance percentages / number of categories * 100

Rubric:
- Parsing nested dictionary structure: 10%
- Category aggregation across months: 10%
- Variance analysis (over/under): 15%
- Calculating savings opportunities: 15%
- Trend calculation and forecasting: 15%
- Budget health score calculation: 15%
- Generating ranked recommendations: 10%
- Comprehensive output formatting: 10%

"""

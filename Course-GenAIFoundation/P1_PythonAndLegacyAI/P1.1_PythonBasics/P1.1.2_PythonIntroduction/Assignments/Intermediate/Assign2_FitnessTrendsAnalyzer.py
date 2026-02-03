"""
Intermediate Assignment 2: Fitness Trends Analyzer

Scenario:
A fitness app tracks daily steps over several weeks and needs to identify weekly trends,
find the best week, and calculate consistency metrics.

Objective:
Analyze weekly step data to find weekly totals, averages, best performing week, and 
days that fell short of the goal.

Inputs:
- weeks_data (list of lists, where each inner list contains 7 days of step counts)
- daily_goal (integer, minimum steps for a day)

Outputs:
- Weekly total and average for each week
- Best performing week number
- Days below goal for each week
- Consistency score (% of days meeting goal)

Steps / Logic Checklist:
1) Parse the nested list structure (weeks and daily values).
2) For each week, calculate total steps and daily average.
3) For each week, count days below the daily goal.
4) Find the week with maximum total steps.
5) Calculate overall consistency score (total days meeting goal / total days).
6) Print formatted report with all metrics.

Constraints:
- At least 2 weeks of data (14 days minimum).
- Each week has exactly 7 days.
- daily_goal is a positive integer.

Example:
Input: weeks_data=[[8000,9200,7500,10000,9500,8800,9100],
                   [9000,8500,9800,10200,8900,9100,9300]]
       daily_goal=9000
Output:
Week 1: Total=62100, Average=8871, Below Goal=4
Week 2: Total=64800, Average=9257, Below Goal=2
Best Week: 2
Consistency: 71%

Hints:
- Use nested loops to iterate weeks and days.
- Use sum() for totals and len() for counting.
- Use list comprehension or count conditions.
- Calculate percentage: (count / total) * 100

Rubric:
- Parsing nested list structure: 15%
- Weekly total and average calculations: 20%
- Counting days below goal per week: 20%
- Finding best performing week: 15%
- Calculating consistency score: 15%
- Formatted output: 15%

"""

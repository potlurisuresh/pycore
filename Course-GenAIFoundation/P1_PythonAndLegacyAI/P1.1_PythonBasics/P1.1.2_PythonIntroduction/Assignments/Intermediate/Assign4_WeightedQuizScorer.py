"""
Intermediate Assignment 4: Weighted Quiz Scorer

Scenario:
An educational platform scores quizzes where questions have different weights/importance.
Some questions are worth more points than others.

Objective:
Score a weighted quiz where each question has a point value, and some may have 
partial credit. Calculate total score, percentage, and performance level.

Inputs:
- questions (list of dicts with keys: 'id', 'max_points')
- user_answers (list of dicts with keys: 'question_id', 'points_earned')
- passing_percentage (float, e.g., 70.0)

Outputs:
- Points earned per question vs max points
- Total points and percentage
- Performance level (Excellent/Good/Fair/Poor)
- Questions that scored below 50%

Steps / Logic Checklist:
1) Parse question structure (extract max points).
2) Parse user answers (extract points earned).
3) For each question, match answer to max_points and calculate percentage.
4) Sum total points earned and total max points.
5) Calculate overall percentage.
6) Determine performance level based on percentage.
7) Identify questions scoring below 50%.
8) Print detailed breakdown.

Constraints:
- User answers list matches number of questions.
- Points earned <= max points for each question.
- Passing percentage is between 0 and 100.

Example:
Input: questions=[{"id": 1, "max_points": 20}, {"id": 2, "max_points": 30}, {"id": 3, "max_points": 50}]
       user_answers=[{"question_id": 1, "points_earned": 18}, 
                     {"question_id": 2, "points_earned": 21},
                     {"question_id": 3, "points_earned": 40}]
       passing_percentage=70
Output:
Q1: 18/20 (90%), Q2: 21/30 (70%), Q3: 40/50 (80%)
Total: 79/100 (79%)
Performance: Good
Questions Below 50%: None

Hints:
- Use list of dictionaries for flexible data structure.
- Use loops to match question IDs with answers.
- Calculate percentage: (points / max) * 100
- Use if/elif for performance levels.
- Track questions that need review.

Rubric:
- Parsing question and answer structures: 15%
- Matching answers to questions: 15%
- Calculating per-question percentages: 15%
- Calculating total points and percentage: 15%
- Determining performance level: 15%
- Identifying weak questions: 15%
- Formatted detailed output: 10%

"""

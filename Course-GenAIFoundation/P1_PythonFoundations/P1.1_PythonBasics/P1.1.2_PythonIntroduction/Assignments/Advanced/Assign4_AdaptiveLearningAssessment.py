"""
Advanced Assignment 4: Adaptive Learning Assessment System

Scenario:
Score an adaptive quiz, analyze learning gaps, and recommend next steps.

Inputs:
- question_bank (id, difficulty, category, max_points, correct_answer)
- student_attempts (question_id, answer, time_spent, confidence)
- mastery_threshold (percentage)

Tasks:
1) Score final attempt per question.
2) Compute per‑category totals and mastery %.
3) Correlate time/confidence with accuracy.
4) Identify weak categories and generate recommendations.

Output:
- Overall score, category mastery, insights, and 3–5 recommendations.

Hints:
- Use dicts keyed by category.
- Mastery = points / max_points * 100.

Rubric:
- Scoring accuracy, mastery analysis, insights, report clarity.
"""

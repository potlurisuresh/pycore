"""
Advanced Assignment 4: Adaptive Learning Assessment System

Scenario:
An educational platform administers adaptive quizzes that adjust difficulty based on
performance. The system must track question attempts, calculate weighted scores with
partial credit, analyze learning gaps, adjust difficulty, and predict mastery level.

Objective:
Score an adaptive quiz where questions adjust in difficulty, calculate comprehensive
performance metrics, identify learning gaps, estimate mastery, and generate personalized
learning recommendations.

Inputs:
- question_bank (list of dicts: {id, difficulty, category, max_points, correct_answer})
- student_attempts (list of dicts: {question_id, attempt_num, answer, time_spent, confidence})
- difficulty_thresholds (dict: {easy, medium, hard} point values)
- mastery_threshold (float, % to consider mastered)
- min_questions_per_category (int, minimum for confidence)

Outputs:
- Overall score and percentage
- Per-category analysis (score, attempts, difficulty)
- Learning gaps (categories below mastery)
- Question difficulty progression
- Time analysis (time spent vs performance correlation)
- Confidence vs accuracy correlation
- Adaptive difficulty recommendations
- Predicted mastery level per category
- Detailed learning report with 5 recommendations

Steps / Logic Checklist:
1) Parse question bank with difficulty levels and categories.
2) Parse student attempts with metadata (time, confidence).
3) Group attempts by question and take final attempt for scoring.
4) Calculate points: correct=max_points, partial_credit based on logic.
5) Calculate per-category totals and percentages.
6) Identify weak categories (score < mastery_threshold).
7) Analyze correlation: time spent vs accuracy, confidence vs accuracy.
8) Calculate question difficulty average per category.
9) Estimate category mastery (score ÷ max possible × 100).
10) Generate adaptive recommendations (review weak categories, practice harder, etc).
11) Format comprehensive assessment report.

Constraints:
- Minimum 10 questions, maximum 100.
- At least 2 attempts per question allowed.
- Time spent recorded in seconds (0-600 range).
- Confidence scale 1-5.
- Categories must have minimum questions for analysis.

Example:
Input: Questions across Math, Science, English (3 categories)
Student attempts 15 questions (5 per category)
Answers: 80% overall, but Science only 60%
Time data: Spends 45s on hard problems, 20s on easy
Confidence avg: 3.8, but accuracy in low-confidence answers: 65%

Output:
OVERALL PERFORMANCE:
Score: 12/15 (80%)
Attempts Average: 1.2 per question
Time Average: 35 seconds

CATEGORY BREAKDOWN:
Math: 5/5 (100%) - Mastered ✓
Science: 3/5 (60%) - Below Mastery ✗
English: 4/5 (80%) - Near Mastery ⚠
Total Questions: 15

LEARNING INSIGHTS:
Time Analysis: Strong correlation - faster responses on mastered topics
Confidence Analysis: High confidence (4-5) = 90% accuracy, Low confidence = 65%
Difficulty Progression: Appropriately challenged on Math, under-challenged on Science

PREDICTED MASTERY:
Math: 95% (1-2 more questions to certify)
Science: 70% (needs 3-4 more practice questions)
English: 85% (borderline, recommend review)

ADAPTIVE RECOMMENDATIONS:
1. Focus on Science fundamentals - 5 practice problems on weak concepts
2. Build confidence on English - review material before retesting
3. Challenge yourself on Math - move to advanced problem set
4. Analyze high-confidence/low-accuracy questions
5. Try spaced repetition on Science - 2-day intervals

Hints:
- Use dict grouping by category for aggregation.
- Partial credit: if answer close (semantic), award 50% points.
- Mastery = (correct_points / max_points) * 100
- Correlation: track (time, accuracy) and (confidence, accuracy) pairs.
- Use sorted() to rank categories by performance.
- Recommendations should be specific to weak areas.

Rubric:
- Parsing question bank and student attempts: 12%
- Scoring with partial credit logic: 12%
- Category-level aggregation: 10%
- Mastery calculation and gap analysis: 12%
- Time/confidence correlation analysis: 12%
- Adaptive recommendation generation: 12%
- Difficulty progression assessment: 10%
- Report formatting and clarity: 8%

"""

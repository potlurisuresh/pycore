"""
Beginner Assignment 4: Simple Quiz Scorer

Scenario:
A teacher wants to auto-score a 3-question quiz.

Objective:
Compare user answers to correct answers and show a result message.

Inputs:
- answers (list of strings)
- user_answers (list of strings)

Outputs:
- Total questions, correct count, and result message.

Steps / Logic Checklist:
1) Loop through answers.
2) Count matches between user_answers and answers.
3) Print total questions and correct count.
4) Print a result message based on score.

Constraints:
- Both lists are the same length.

Example:
Input: answers=["4","8","6"], user_answers=["4","7","6"]
Output: Correct=2, Result: Good Job

Hints:
- Use a loop with indexes or zip().
- Use if/elif/else for result message.
- Use .format() for output formatting.

"""

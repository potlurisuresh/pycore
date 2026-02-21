"""
Beginner Assignment 5: File Path Processor

Scenario:
Extract the filename and extension from a complete file path.

Input:
- filepath: "C:/Users/Documents/report.pdf"

Tasks:
1. Split the path by '/' to get parts
2. Get the last part (filename with extension)
3. Split the filename by '.' to separate name and extension
4. Print the directory, filename, and extension

Expected Output:
Directory: C:/Users/Documents
Filename: report
Extension: pdf

Hints:
- Use split('/') to get path parts
- Use [-1] to get last element
- Use split('.') on filename
- Use join() to reconstruct directory

Rubric:
- Correct path splitting: 30%
- Correct filename extraction: 25%
- Correct extension extraction: 25%
- Proper output: 20%
"""

# Input data
filepath = "C:/Users/Documents/report.pdf"

# Your code here

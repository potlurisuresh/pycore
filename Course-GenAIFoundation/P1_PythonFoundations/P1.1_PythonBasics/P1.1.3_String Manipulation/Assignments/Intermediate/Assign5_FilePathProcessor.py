"""
Intermediate Assignment 5: File Path Processor

Scenario:
Process multiple file paths, categorize by extension, and generate file statistics.

Input:
- file_list: "C:/docs/report.pdf|D:/images/photo.jpg|E:/data/info.txt|C:/docs/summary.pdf"

Tasks:
1. Split file_list by '|' to get individual paths
2. For each path, extract directory, filename, and extension
3. Count files by extension
4. Find all PDF files
5. Print file inventory and statistics

Expected Output:
File Inventory
--------------
Total Files: 4

Extension Statistics:
pdf: 2 files
jpg: 1 files
txt: 1 files

PDF Files:
1. report.pdf (Location: C:/docs)
2. summary.pdf (Location: C:/docs)

File Details:
C:/docs/report.pdf
  - Name: report
  - Extension: pdf
  - Directory: C:/docs

D:/images/photo.jpg
  - Name: photo
  - Extension: jpg
  - Directory: D:/images

(etc.)

Hints:
- Use split('|') for paths
- Use split('/') for path parts
- Use split('.') for filename
- Track extensions in lists
- Use count() for statistics

Rubric:
- Correct path parsing: 25%
- Correct component extraction: 25%
- Correct extension counting: 25%
- Correct PDF filtering: 15%
- Proper output: 10%
"""

# Input data
file_list = "C:/docs/report.pdf|D:/images/photo.jpg|E:/data/info.txt|C:/docs/summary.pdf"

# Your code here

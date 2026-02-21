"""
Advanced Assignment 5: File Path Processor

Scenario:
Build a file system analytics tool that parses paths, categorizes files by type,
detects naming patterns, identifies duplicates, and generates storage insights.

Input:
- path_database: Multi-line file paths
  "/home/user/documents/report_2024.pdf, C:\\Users\\Admin\\Photos\\vacation.jpg
   /var/log/system.log, /home/user/documents/report_2023.pdf
   invalid\\path, /home/user/music/song.mp3, C:\\Users\\Admin\\Photos\\sunset.jpg
   /home/user/documents/budget_2024.xlsx, /var/log/error.log"

Tasks:
1. Parse and normalize all paths:
   - Detect OS type (Unix: /, Windows: \)
   - Extract components: directory, filename, extension
   - Handle invalid paths
2. Categorize files by extension:
   - Documents: .pdf, .xlsx, .docx
   - Media: .jpg, .png, .mp3, .mp4
   - Logs: .log, .txt
   - Unknown: no extension or unrecognized
3. Detect file patterns:
   - Naming conventions (report_YEAR, file_version)
   - Duplicate filenames (same name, different paths)
   - Sequential files (report_2023, report_2024)
   - Date patterns in filenames
4. Analyze directory structure:
   - Most common directories
   - File concentration (files per directory)
   - Cross-platform paths detected
5. Generate file system intelligence report with recommendations

Expected Output:
File System Analytics Report
==============================

Path Processing Summary:
Total Paths: 9
Valid Paths: 8
Invalid Paths: 1
Cross-Platform Detection: Windows (2), Unix (6)

File Type Distribution:
Documents: 3 files (37.5%)
  - PDF: 2 files (report_2024.pdf, report_2023.pdf)
  - XLSX: 1 files (budget_2024.xlsx)

Media: 3 files (37.5%)
  - JPG: 2 files (vacation.jpg, sunset.jpg)
  - MP3: 1 files (song.mp3)

Logs: 2 files (25.0%)
  - LOG: 2 files (system.log, error.log)

Directory Analysis:
/home/user/documents: 3 files (37.5%)
  - Highest concentration
  - File types: PDF, XLSX
  - Pattern detected: yearly reports (2023, 2024)

C:\Users\Admin\Photos: 2 files (25.0%)
  - File types: JPG
  - Pattern: photo collection

/var/log: 2 files (25.0%)
  - File types: LOG
  - System logs location

/home/user/music: 1 files (12.5%)
  - File types: MP3

Naming Pattern Detection:
Sequential Files:
  - report_2023.pdf -> report_2024.pdf
    Location: /home/user/documents
    Pattern: Annual reports (YEAR suffix)

Date Patterns:
  - Files with year markers: 3 files
    2024: budget_2024.xlsx, report_2024.pdf
    2023: report_2023.pdf

File Type Clusters:
  - Photos clustered in: C:\Users\Admin\Photos
  - Documents clustered in: /home/user/documents
  - Logs clustered in: /var/log

Storage Insights:
- Documents directory showing yearly pattern (2023-2024)
- Media files properly organized in Photos folder
- System logs centralized in /var/log
- Cross-platform paths detected (2 Windows, 6 Unix)

Path Anomalies:
WARNING: Invalid path format: invalid\path
WARNING: Relative vs Absolute: All valid paths are absolute

File Organization Score: 85/100
+ Well-organized by type
+ Clear directory structure
+ Sequential naming for reports
- Mixed OS paths (migration needed?)

Recommendations:
1. Standardize path format (choose Windows or Unix)
2. Continue yearly naming convention for documents
3. Consider archiving pre-2024 files
4. Maintain type-based directory organization
5. Investigate invalid path: invalid\path

Hints:
- Detect OS by checking '\' vs '/'
- Use split() with appropriate separator
- Extract extension with split('.')[-1]
- Find patterns by comparing filenames
- Track directory frequency

Rubric:
- Path parsing accuracy: 20%
- File categorization: 15%
- Pattern detection: 25%
- Directory analysis: 20%
- Actionable insights: 20%
"""

# Input data
path_database = """/home/user/documents/report_2024.pdf, C:\\Users\\Admin\\Photos\\vacation.jpg
/var/log/system.log, /home/user/documents/report_2023.pdf
invalid\\path, /home/user/music/song.mp3, C:\\Users\\Admin\\Photos\\sunset.jpg
/home/user/documents/budget_2024.xlsx, /var/log/error.log"""

# Your code here

"""
Advanced Assignment 1: Log Entry Parser

Scenario:
You are building a log analytics helper that parses timestamped log lines,
finds repeated errors, computes time gaps, and extracts metadata via regex.

Input:
- log_stream: Multi-line log data
  "2026-02-03 14:30:15 ERROR Database connection failed - Retry attempt 1
  2026-02-03 14:30:20 INFO User:admin login successful from IP:192.168.1.1
  2026-02-03 14:30:25 ERROR Database connection failed - Retry attempt 2
  2026-02-03 14:30:30 WARNING Low memory: 15% available
  2026-02-03 14:30:35 ERROR Database connection failed - Retry attempt 3
  2026-02-03 14:30:40 INFO System backup completed successfully
  2026-02-03 14:31:00 CRITICAL Service crashed - immediate action required"

Tasks:
1) Parse each entry into (timestamp, level, message).
2) Count entries by level and identify repeated ERROR messages.
3) Compute time span between the first and last related errors.
4) Extract metadata with regex:
  - Users: r"User:(\w+)"
  - IPs: r"IP:(\d+\.\d+\.\d+\.\d+)"
  - Percentages: r"(\d+)%"
5) Detect an error burst: 3+ errors within 30 seconds.
6) Print a compact report with summary + insights.

Expected Output (sample):
- Total Entries: 7
- By Level: CRITICAL=1, ERROR=3, WARNING=1, INFO=2
- Repeated Error: "Database connection failed" (3x)
- Burst Detected: True (20s window)
- Users: admin | IPs: 192.168.1.1 | Percentages: 15

Hints:
- Convert timestamps to seconds to compute intervals.
- Use dictionaries for counts and repeats.
- Keep output compact but readable.

Rubric:
- Parsing accuracy: 20%
- Pattern detection: 20%
- Time calculations: 20%
- Regex extraction: 20%
- Report clarity: 20%
"""

# Input data
log_stream = """2026-02-03 14:30:15 ERROR Database connection failed - Retry attempt 1
2026-02-03 14:30:20 INFO User:admin login successful from IP:192.168.1.1
2026-02-03 14:30:25 ERROR Database connection failed - Retry attempt 2
2026-02-03 14:30:30 WARNING Low memory: 15% available
2026-02-03 14:30:35 ERROR Database connection failed - Retry attempt 3
2026-02-03 14:30:40 INFO System backup completed successfully
2026-02-03 14:31:00 CRITICAL Service crashed - immediate action required"""

# Your code here

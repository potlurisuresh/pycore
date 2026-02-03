"""
Advanced Assignment 1: Log Entry Parser

Scenario:
Build a comprehensive log analysis system that parses multi-format logs,
detects error patterns, calculates time intervals, and generates insights.

Input:
- log_stream: Multi-line log data with varying formats
  "2026-02-03 14:30:15 ERROR Database connection failed - Retry attempt 1
   2026-02-03 14:30:20 INFO User:admin login successful from IP:192.168.1.1
   2026-02-03 14:30:25 ERROR Database connection failed - Retry attempt 2
   2026-02-03 14:30:30 WARNING Low memory: 15% available
   2026-02-03 14:30:35 ERROR Database connection failed - Retry attempt 3
   2026-02-03 14:30:40 INFO System backup completed successfully
   2026-02-03 14:31:00 CRITICAL Service crashed - immediate action required"

Tasks:
1. Parse all log entries (timestamp, level, message)
2. Detect repeated error patterns (same error message multiple times)
3. Calculate time intervals between related errors
4. Extract structured data using regex:
   - User mentions: r"User:(\w+)"
   - IP addresses: r"IP:(\d+\.\d+\.\d+\.\d+)"
   - Percentages: r"(\d+)%"
5. Count entries by severity (CRITICAL > ERROR > WARNING > INFO)
6. Identify error bursts (3+ errors within 30 seconds)
7. Generate comprehensive analysis report

Expected Output:
Advanced Log Analysis Report
=============================

Summary Statistics:
Total Entries: 7
By Level: CRITICAL=1, ERROR=3, WARNING=1, INFO=2

Critical Issues:
WARNING: CRITICAL: [14:31:00] Service crashed - immediate action required

Error Pattern Detection:
Pattern: "Database connection failed"
  Occurrences: 3
  First seen: 14:30:15
  Last seen: 14:30:35
  Time span: 20 seconds
  Status: ERROR BURST DETECTED (3 errors in 20s)

Extracted Metadata:
Users mentioned: admin
IP addresses: 192.168.1.1
System metrics: 15% (memory available)

Timeline Analysis:
14:30:15-14:30:35 -> ERROR burst (3 occurrences, 20s duration)
14:30:30 -> WARNING: Low memory detected
14:31:00 -> CRITICAL: Service crash

Recommendations:
1. Investigate database connectivity (3 failed attempts in 20s)
2. Check system memory (only 15% available)
3. Immediate attention required for service crash

Hints:
- Parse timestamp to calculate intervals
- Use regex for pattern extraction
- Track error messages in lists
- Calculate time differences
- Detect bursts with timestamps

Rubric:
- Correct parsing of all entries: 15%
- Pattern detection: 20%
- Time interval calculation: 20%
- Regex extraction: 20%
- Burst detection: 15%
- Comprehensive report: 10%
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

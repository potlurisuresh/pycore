"""
Beginner Solution 5: File Path Processor
"""

# Input data
file_path = "/home/user/documents/report.pdf"

# Detect OS type
if "\\" in file_path:
    os_type = "Windows"
    separator = "\\"
else:
    os_type = "Unix/Linux"
    separator = "/"

# Split path to get filename
parts = file_path.split(separator)
filename = parts[-1]  # Last part is the filename

# Extract name and extension
name_parts = filename.split(".")
name = name_parts[0]
extension = name_parts[1]

# Print formatted output
print("File Path Processor")
print("=" * 20)
print(f"Full Path: {file_path}")
print(f"OS Type: {os_type}")
print(f"Filename: {filename}")
print(f"Name: {name}")
print(f"Extension: {extension}")

"""
Intermediate Solution 5: File Path Processor
"""

# Input data
path_list = "/home/user/docs/report.pdf, C:\\Users\\file.txt, /var/log/system.log"

# Parse paths
paths = path_list.split(", ")

# Initialize lists
valid_paths = []
extensions = []
os_types = []

# Process each path
for path in paths:
    path_clean = path.strip()
    
    # Detect OS
    if "\\" in path_clean:
        os_type = "Windows"
        separator = "\\"
    else:
        os_type = "Unix"
        separator = "/"
    
    os_types.append(os_type)
    
    # Extract filename and extension
    parts = path_clean.split(separator)
    filename = parts[-1]
    
    if "." in filename:
        name_parts = filename.split(".")
        extension = name_parts[-1]
        extensions.append(extension)
        valid_paths.append(path_clean)

# Count extensions
ext_names = []
ext_counts = []
for ext in extensions:
    if ext not in ext_names:
        ext_names.append(ext)
        ext_counts.append(extensions.count(ext))

# Print formatted output
print("File Path Analysis Report")
print("=" * 30)
print(f"Total Paths: {len(paths)}")
print(f"Valid Paths: {len(valid_paths)}")
print()
print("Extension Statistics:")
for i in range(len(ext_names)):
    print(f"  .{ext_names[i]}: {ext_counts[i]} file(s)")
print()
print("Paths by OS:")
for i in range(len(valid_paths)):
    print(f"  [{os_types[i]}] {valid_paths[i]}")

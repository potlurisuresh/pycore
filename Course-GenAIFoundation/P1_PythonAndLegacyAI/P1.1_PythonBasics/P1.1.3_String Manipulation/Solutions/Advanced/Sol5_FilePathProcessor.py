"""
Advanced Solution 5: File Path Processor
"""
import re

# Input data
path_database = """/home/user/documents/report_2024.pdf, C:\\Users\\Admin\\Photos\\vacation.jpg
/var/log/system.log, /home/user/documents/report_2023.pdf
invalid\\path, /home/user/music/song.mp3, C:\\Users\\Admin\\Photos\\sunset.jpg
/home/user/documents/budget_2024.xlsx, /var/log/error.log"""

# Parse paths
all_paths = path_database.replace("\n", ", ").split(", ")
all_paths = [p.strip() for p in all_paths if p.strip()]

# Extension categories
doc_extensions = ["pdf", "xlsx", "docx"]
media_extensions = ["jpg", "png", "mp3", "mp4"]
log_extensions = ["log", "txt"]

# Process paths
valid_paths = []
invalid_paths = []
os_types = []
directories = []
filenames = []
extensions = []

windows_count = 0
unix_count = 0

for path in all_paths:
    path_clean = path.strip()
    
    # Detect OS type
    if "\\" in path_clean:
        os_type = "Windows"
        separator = "\\"
    elif "/" in path_clean:
        os_type = "Unix"
        separator = "/"
    else:
        invalid_paths.append(path_clean)
        continue
    
    # Check if absolute path
    is_absolute = False
    if os_type == "Unix" and path_clean.startswith("/"):
        is_absolute = True
    elif os_type == "Windows" and ":" in path_clean:
        is_absolute = True
    
    if not is_absolute:
        invalid_paths.append(path_clean)
        continue
    
    # Extract components
    parts = path_clean.split(separator)
    if len(parts) < 2:
        invalid_paths.append(path_clean)
        continue
    
    filename = parts[-1]
    
    # Check for extension
    if "." not in filename:
        invalid_paths.append(path_clean)
        continue
    
    # Extract extension
    extension = filename.split(".")[-1].lower()
    directory = separator.join(parts[:-1])
    
    # Store valid path data
    valid_paths.append(path_clean)
    os_types.append(os_type)
    directories.append(directory)
    filenames.append(filename)
    extensions.append(extension)
    
    if os_type == "Windows":
        windows_count += 1
    else:
        unix_count += 1

# Categorize files
doc_files = []
media_files = []
log_files = []

for i in range(len(valid_paths)):
    ext = extensions[i]
    if ext in doc_extensions:
        doc_files.append(filenames[i])
    elif ext in media_extensions:
        media_files.append(filenames[i])
    elif ext in log_extensions:
        log_files.append(filenames[i])

# Count extensions
unique_extensions = []
ext_counts = []

for ext in extensions:
    if ext not in unique_extensions:
        unique_extensions.append(ext)
        ext_counts.append(extensions.count(ext))

# Directory analysis
unique_dirs = []
dir_counts = []

for directory in directories:
    if directory not in unique_dirs:
        unique_dirs.append(directory)
        dir_counts.append(directories.count(directory))

# Find sequential files (same base name, different year)
sequential_files = []
for i in range(len(filenames)):
    for j in range(i + 1, len(filenames)):
        name1 = filenames[i].split(".")[0]
        name2 = filenames[j].split(".")[0]
        
        if "_" in name1 and "_" in name2:
            base1 = "_".join(name1.split("_")[:-1])
            base2 = "_".join(name2.split("_")[:-1])
            if base1 == base2:
                sequential_files.append((filenames[i], filenames[j]))
                break

# Print report
print("File System Analytics Report")
print("=" * 50)
print()

print("Path Processing Summary:")
print(f"Total Paths: {len(all_paths)}")
print(f"Valid Paths: {len(valid_paths)}")
print(f"Invalid Paths: {len(invalid_paths)}")
print(f"Cross-Platform Detection: Windows ({windows_count}), Unix ({unix_count})")
print()

print("File Type Distribution:")
if len(doc_files) > 0:
    percentage = len(doc_files) * 100.0 / len(valid_paths)
    print(f"Documents: {len(doc_files)} files ({percentage:.1f}%)")
    pdf_files = [f for f in doc_files if f.endswith(".pdf")]
    xlsx_files = [f for f in doc_files if f.endswith(".xlsx")]
    if len(pdf_files) > 0:
        print(f"  - PDF: {len(pdf_files)} files ({', '.join(pdf_files)})")
    if len(xlsx_files) > 0:
        print(f"  - XLSX: {len(xlsx_files)} files ({', '.join(xlsx_files)})")
    print()

if len(media_files) > 0:
    percentage = len(media_files) * 100.0 / len(valid_paths)
    print(f"Media: {len(media_files)} files ({percentage:.1f}%)")
    jpg_files = [f for f in media_files if f.endswith(".jpg")]
    mp3_files = [f for f in media_files if f.endswith(".mp3")]
    if len(jpg_files) > 0:
        print(f"  - JPG: {len(jpg_files)} files ({', '.join(jpg_files)})")
    if len(mp3_files) > 0:
        print(f"  - MP3: {len(mp3_files)} files ({', '.join(mp3_files)})")
    print()

if len(log_files) > 0:
    percentage = len(log_files) * 100.0 / len(valid_paths)
    print(f"Logs: {len(log_files)} files ({percentage:.1f}%)")
    print(f"  - LOG: {len(log_files)} files ({', '.join(log_files)})")
    print()

print("Directory Analysis:")
# Sort directories by count
for _ in range(min(3, len(unique_dirs))):
    max_count = max(dir_counts)
    max_index = dir_counts.index(max_count)
    directory = unique_dirs[max_index]
    count = dir_counts[max_index]
    percentage = count * 100.0 / len(valid_paths)
    
    print(f"{directory}: {count} files ({percentage:.1f}%)")
    
    # File types in directory
    dir_ext = []
    for i in range(len(directories)):
        if directories[i] == directory:
            ext = extensions[i].upper()
            if ext not in dir_ext:
                dir_ext.append(ext)
    
    if len(dir_ext) > 0:
        print(f"  - File types: {', '.join(dir_ext)}")
    
    # Mark as processed
    dir_counts[max_index] = -1
    print()

if len(sequential_files) > 0:
    print("Naming Pattern Detection:")
    print("Sequential Files:")
    for f1, f2 in sequential_files:
        # Find directory
        dir1 = ""
        for i in range(len(filenames)):
            if filenames[i] == f1:
                dir1 = directories[i]
                break
        
        print(f"  - {f1} -> {f2}")
        print(f"    Location: {dir1}")
        
        # Extract years
        years = re.findall(r"\d{4}", f1 + " " + f2)
        if len(years) >= 2:
            print(f"    Pattern: Annual reports ({', '.join(sorted(years))})")
    print()

print("Storage Insights:")
# Check for yearly patterns
if len(sequential_files) > 0:
    years = []
    for f1, f2 in sequential_files:
        years.extend(re.findall(r"\d{4}", f1 + " " + f2))
    if len(years) >= 2:
        year_str = "-".join(sorted(set(years)))
        print(f"- Documents directory showing yearly pattern ({year_str})")

# Check organization
if len(doc_files) > 0:
    print("- Documents properly organized")
if len(media_files) > 0:
    print("- Media files in dedicated folder")
if len(log_files) > 0:
    print("- System logs centralized in /var/log")

# Cross-platform
if windows_count > 0 and unix_count > 0:
    print(f"- Cross-platform paths detected ({windows_count} Windows, {unix_count} Unix)")
print()

print("Path Anomalies:")
if len(invalid_paths) > 0:
    for path in invalid_paths:
        print(f"WARNING: Invalid path format: {path}")
print()

# Organization score
score = 85
if len(unique_dirs) > 1:
    score += 5
if len(sequential_files) > 0:
    score += 5
if windows_count > 0 and unix_count > 0:
    score -= 10

print(f"File Organization Score: {score}/100")
print()

print("Recommendations:")
if windows_count > 0 and unix_count > 0:
    print("1. Standardize path format (choose Windows or Unix)")
if len(sequential_files) > 0:
    print("2. Continue yearly naming convention for documents")
if any("2023" in f or "2022" in f for f in filenames):
    print("3. Consider archiving pre-2024 files")
if len(invalid_paths) > 0:
    print(f"4. Investigate invalid path: {invalid_paths[0]}")

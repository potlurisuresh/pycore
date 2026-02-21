"""
Advanced Solution 5: File Path Processor (Concise)
"""
import re

# Input data
path_database = """/home/user/documents/report_2024.pdf, C:\\Users\\Admin\\Photos\\vacation.jpg
/var/log/system.log, /home/user/documents/report_2023.pdf
invalid\\path, /home/user/music/song.mp3, C:\\Users\\Admin\\Photos\\sunset.jpg
/home/user/documents/budget_2024.xlsx, /var/log/error.log"""

all_paths = [p.strip() for p in path_database.replace("\n", ", ").split(", ") if p.strip()]

doc_ext = {"pdf", "xlsx", "docx"}
media_ext = {"jpg", "png", "mp3", "mp4"}
log_ext = {"log", "txt"}

valid = []
invalid = []
directories = []
filenames = []
extensions = []
os_types = []

for path in all_paths:
    if "\\" in path:
        os_type, sep = "Windows", "\\"
    elif "/" in path:
        os_type, sep = "Unix", "/"
    else:
        invalid.append(path)
        continue

    is_absolute = (os_type == "Unix" and path.startswith("/")) or (os_type == "Windows" and ":" in path)
    if not is_absolute or sep not in path:
        invalid.append(path)
        continue

    parts = path.split(sep)
    filename = parts[-1]
    if "." not in filename:
        invalid.append(path)
        continue

    directory = sep.join(parts[:-1])
    ext = filename.split(".")[-1].lower()

    valid.append(path)
    os_types.append(os_type)
    directories.append(directory)
    filenames.append(filename)
    extensions.append(ext)

def count_map(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts

doc_files = [f for f, e in zip(filenames, extensions) if e in doc_ext]
media_files = [f for f, e in zip(filenames, extensions) if e in media_ext]
log_files = [f for f, e in zip(filenames, extensions) if e in log_ext]

dir_counts = count_map(directories)

sequential = []
for i, name1 in enumerate(filenames):
    base1 = "_".join(name1.split(".")[0].split("_")[:-1])
    for j, name2 in enumerate(filenames):
        if j <= i:
            continue
        base2 = "_".join(name2.split(".")[0].split("_")[:-1])
        if base1 and base1 == base2:
            sequential.append((name1, name2))
            break

print("File System Analytics")
print("=" * 48)
print(f"Total: {len(all_paths)} | Valid: {len(valid)} | Invalid: {len(invalid)}")
print(f"Windows: {os_types.count('Windows')} | Unix: {os_types.count('Unix')}")

print("\nFile Types:")
print(f"- Documents: {len(doc_files)}")
print(f"- Media: {len(media_files)}")
print(f"- Logs: {len(log_files)}")

print("\nTop Directories:")
for directory, count in sorted(dir_counts.items(), key=lambda x: (-x[1], x[0]))[:3]:
    print(f"- {directory}: {count}")

if sequential:
    print("\nSequential Files:")
    for f1, f2 in sequential:
        years = re.findall(r"\d{4}", f1 + " " + f2)
        tag = f" ({'-'.join(sorted(set(years)))})" if years else ""
        print(f"- {f1} -> {f2}{tag}")

print("\nAnomalies:")
for path in invalid:
    print(f"- Invalid: {path}")
print("\nRecommendations:")
if os_types.count("Windows") > 0 and os_types.count("Unix") > 0:
    print("- Standardize path format (choose Windows or Unix)")
if sequential:
    print("- Continue yearly naming convention for documents")
if any("2023" in f or "2022" in f for f in filenames):
    print("- Consider archiving pre-2024 files")
if invalid:
    print(f"- Investigate invalid path: {invalid[0]}")

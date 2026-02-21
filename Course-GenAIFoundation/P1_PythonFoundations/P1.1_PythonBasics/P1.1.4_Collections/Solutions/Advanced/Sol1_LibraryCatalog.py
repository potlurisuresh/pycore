"""
Advanced Solution 1: Library Book Catalog
"""

# Input data
book_data = """Sci-Fi|The Martian|Andy Weir|2014
Fiction|To Kill a Mockingbird|Harper Lee|1960
Fiction|The Road|Cormac McCarthy|2006
Sci-Fi|Dune|Frank Herbert|1965
Sci-Fi|Foundation|Isaac Asimov|1951"""

# Advanced structures
by_genre_year = {}  # (genre, year) -> [books]
word_index = {}  # word -> {book titles}
decade_stats = {}  # decade -> count

for line in book_data.split('\n'):
    genre, title, author, year = line.split('|')
    year = int(year)
    decade = (year // 10) * 10
    
    # Tuple keys for grouping
    key = (genre, year)
    if key not in by_genre_year:
        by_genre_year[key] = []
    by_genre_year[key].append(title)
    
    # Inverted index
    for word in title.lower().split():
        if word not in word_index:
            word_index[word] = set()
        word_index[word].add(title)
    
    # Decade statistics
    decade_stats[decade] = decade_stats.get(decade, 0) + 1

print("Books by (Genre, Year):")
for key, books in sorted(by_genre_year.items()):
    print(f"{key}: {books}")

print("\nWord Index (sample):")
for word, titles in list(word_index.items())[:3]:
    print(f"'{word}': {titles}")

print("\nDecade Statistics:")
for decade, count in sorted(decade_stats.items()):
    print(f"{decade}s: {count} books")

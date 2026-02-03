"""
Beginner Solution 1: Library Book Catalog
"""

# Input data
book_record = "Sci-Fi|The Martian|Andy Weir|2014"

# Parse and create nested structure
parts = book_record.split('|')
genre = parts[0]

# Create nested dictionary: genre -> book details
catalog = {
    genre: {
        'title': parts[1],
        'author': parts[2],
        'year': int(parts[3])
    }
}

print("Library Catalog:")
print(catalog)
print(f"\nGenre: {genre}")
print(f"Book details: {catalog[genre]}")

"""
Intermediate Solution 1: Library Book Catalog
"""

# Input data
book_data = """Sci-Fi|The Martian|Andy Weir|2014
Fiction|To Kill a Mockingbird|Harper Lee|1960
Fiction|The Road|Cormac McCarthy|2006
Sci-Fi|Dune|Frank Herbert|1965"""

# Build nested structure: genre -> author -> [books]
catalog = {}

for line in book_data.split('\n'):
    genre, title, author, year = line.split('|')
    
    # Create genre if not exists
    if genre not in catalog:
        catalog[genre] = {}
    
    # Create author if not exists
    if author not in catalog[genre]:
        catalog[genre][author] = []
    
    # Add book
    catalog[genre][author].append(title)

# Display nested structure
print("Library Catalog (Genre -> Author -> Books):")
for genre, authors in catalog.items():
    print(f"\n{genre}:")
    for author, books in authors.items():
        print(f"  {author}: {books}")

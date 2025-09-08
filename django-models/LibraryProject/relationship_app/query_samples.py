# This file demonstrates some common Django ORM queries.

# Make sure to import the models you need to query.
# The names here are assumed based on a typical library project structure.
from .models import Book, Author, Library, Student, Loan, Librarian

# A simple function to get all books.
def get_all_books():
    """
    Retrieves all Book objects from the database.
    Returns a QuerySet.
    """
    return Book.objects.all()

# A function to get a single library by its name.
def get_library_by_name(library_name):
    """
    Retrieves a single Library object by its name.
    
    If the library does not exist, it will raise a DoesNotExist exception.
    Use try-except blocks to handle this gracefully.
    """
    try:
        library = Library.objects.get(name=library_name)
        print(f"Found library: {library.name}")
        return library
    except Library.DoesNotExist:
        print(f"Error: Library with name '{library_name}' does not exist.")
        return None

# A function to find books published after a certain year.
def find_recent_books(year):
    """
    Finds all books published after the specified year.
    Returns a QuerySet.
    """
    return Book.objects.filter(publication_year__gt=year)

# This new function demonstrates the use of a reverse relationship.
def get_author_books(author_first_name, author_last_name):
    """
    Retrieves all books written by a specific author using the reverse relationship.
    
    This query uses the reverse manager 'books' that Django automatically creates.
    """
    try:
        author = Author.objects.get(first_name=author_first_name, last_name=author_last_name)
        
        books = author.books.all()
        
        if books.exists():
            print(f"Found the following books by {author.first_name} {author.last_name}:")
            for book in books:
                print(f" - {book.title}")
        else:
            print(f"No books found for author {author.first_name} {author.last_name}.")
            
        return books
        
    except Author.DoesNotExist:
        print(f"Error: Author '{author_first_name} {author_last_name}' does not exist.")
        return None
        
# This function demonstrates retrieving an author and then filtering books based on that author object.
def get_books_by_author_object(author_first_name, author_last_name):
    """
    First, it retrieves a single Author object.
    Then, it uses that object to filter the Book queryset.
    """
    try:
        author = Author.objects.get(first_name=author_first_name, last_name=author_last_name)
        
        books = Book.objects.filter(author=author)
        
        if books.exists():
            print(f"Found the following books using the author object for {author.first_name} {author.last_name}:")
            for book in books:
                print(f" - {book.title}")
        else:
            print(f"No books found for this author using the object filter method.")
            
        return books
    
    except Author.DoesNotExist:
        print(f"Error: Author '{author_first_name} {author_last_name}' does not exist.")
        return None

# This function retrieves an Author object using a 'name' field.
def get_author_by_name(author_name):
    """
    Retrieves a single Author object by its name.
    
    NOTE: This query assumes your Author model has a single 'name' field.
    """
    try:
        author = Author.objects.get(name=author_name)
        print(f"Found author: {author.name}")
        return author
    except Author.DoesNotExist:
        print(f"Error: Author with name '{author_name}' does not exist.")
        return None

# This new function retrieves a Librarian object based on a related Library object.
def get_librarian_by_library_name(library_name):
    """
    Retrieves a Librarian object for a given library name.
    
    This demonstrates getting a related object by filtering on a foreign key relationship.
    """
    try:
        # First, retrieve the Library object.
        library = Library.objects.get(name=library_name)
        
        # Then, use that object to find the related Librarian.
        librarian = Librarian.objects.get(library=library)
        
        print(f"Found librarian '{librarian.name}' for the library '{library.name}'.")
        return librarian
    except Library.DoesNotExist:
        print(f"Error: Library with name '{library_name}' does not exist.")
        return None
    except Librarian.DoesNotExist:
        print(f"Error: No librarian found for library '{library_name}'.")
        return None


# Example usage of the functions
def run_queries():
    # First, make sure you have some data to work with.
    # If your database is empty, these queries will return nothing.
    # You might want to create some test data first.
    
    print("--- Getting all books ---")
    all_books = get_all_books()
    for book in all_books:
        print(f" - {book.title} by {book.author.first_name} {book.author.last_name}")

    print("\n--- Getting a specific library ---")
    get_library_by_name("Central Library") # Replace with a library name you have

    print("\n--- Finding recent books ---")
    recent_books = find_recent_books(2020)
    if recent_books.exists():
        print("Found the following books published after 2020:")
        for book in recent_books:
            print(f" - {book.title} ({book.publication_year})")
    else:
        print("No books found published after 2020.")

    print("\n--- Finding books by a specific author using the reverse relationship ---")
    get_author_books("Thabang", "Moalusi") # Replace with an author from your data
    
    print("\n--- Finding books by a specific author using the author object filter ---")
    get_books_by_author_object("Thabang", "Moalusi") # Replace with the same author

    print("\n--- Getting a specific author by name ---")
    get_author_by_name("Thabang Moalusi") # Replace with a valid author name from your data.
    
    print("\n--- Getting a librarian by library name ---")
    get_librarian_by_library_name("Central Library") # Replace with a valid library name.

# If you run this file directly, it will execute the queries.
if __name__ == "__main__":
    run_queries()

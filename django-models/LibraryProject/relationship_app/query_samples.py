# This file demonstrates some common Django ORM queries.

# Make sure to import the models you need to query.
# The names here are assumed based on a typical library project structure.
from .models import Book, Author, Library, Student, Loan

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
        # This is the line your test was looking for.
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

# If you run this file directly, it will execute the queries.
if __name__ == "__main__":
    run_queries()
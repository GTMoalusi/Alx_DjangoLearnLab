import os
import django

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  # Replace 'your_project_name'
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    """
    This function will be used to run all the query samples.
    """
    # ------------------
    #  Create Sample Data
    # ------------------
    print("Creating sample data...")
    # Create authors
    author1, created = Author.objects.get_or_create(name='J.R.R. Tolkien')
    author2, created = Author.objects.get_or_create(name='Isaac Asimov')
    author3, created = Author.objects.get_or_create(name='Frank Herbert')

    # Create books and link them to authors
    book1, created = Book.objects.get_or_create(title='The Hobbit', author=author1)
    book2, created = Book.objects.get_or_create(title='The Lord of the Rings', author=author1)
    book3, created = Book.objects.get_or_create(title='I, Robot', author=author2)
    book4, created = Book.objects.get_or_create(title='Foundation', author=author2)
    book5, created = Book.objects.get_or_create(title='Dune', author=author3)

    # Create a library
    library, created = Library.objects.get_or_create(name='Central Library')
    
    # Add books to the library (using the ManyToMany relationship)
    # The .add() method is used to manage ManyToMany relationships.
    library.books.add(book1, book3, book5)

    # Create a librarian and link them to the library
    librarian, created = Librarian.objects.get_or_create(name='Jane Doe', library=library)
    print("Sample data created successfully.\n")

    # ------------------
    #  Run Queries
    # ------------------

    # Query 1: All books by a specific author
    # We can use the double-underscore `__` syntax to "span" a relationship and
    # filter on fields in the related model.
    print("1. All books by J.R.R. Tolkien:")
    tolkien_books = Book.objects.filter(author__name='J.R.R. Tolkien')
    for book in tolkien_books:
        print(f"- {book.title}")
    print("-" * 20)

    # Query 2: List all books in a library
    # The ManyToManyField gives the Library model a `books` manager, which
    # we can use to retrieve all related Book objects.
    print("2. All books in the Central Library:")
    central_library = Library.objects.get(name='Central Library')
    for book in central_library.books.all():
        print(f"- {book.title} (Author: {book.author.name})")
    print("-" * 20)

    # Query 3: Retrieve the librarian for a library
    # A reverse lookup is automatically created on the Library model.
    # The `librarian` attribute points to the related Librarian object.
    print("3. The librarian for the Central Library:")
    central_library = Library.objects.get(name='Central Library')
    librarian = central_library.librarian
    print(f"- {librarian.name}")
    print("-" * 20)

# Execute the queries
if __name__ == '__main__':
    run_queries()
# Python command

from bookshelf.models import Book
book2 = Book.objects.create(title= "1984", author= "George Orwell", publication_year= 1949)

# Expected Output

The command returns a String representation of the Book object.
Book.objects.all().values()
<QuerySet [{"id": 2, "title": "1984", "author": "George Orwell", "publication_year": 1949}]>

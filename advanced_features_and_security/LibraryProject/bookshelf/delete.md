# Python command

from bookshelf.models import Book
book.title = "Nineteen Eighty-Four"

book.delete()
print(Book.objects.filter(author= "George Orwell").count())

# Expected Outcome

0

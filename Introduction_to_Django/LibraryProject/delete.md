# Python command

from bookshelf.models import Book
book2_instance.title = "Nineteen Eighty-Four"

book2_instance.delete()
print(Book.objects.filter(author= "George Orwell").count())

# Expected Outcome

0

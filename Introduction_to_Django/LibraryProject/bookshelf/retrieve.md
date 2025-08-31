# Python command

from bookshelf.models import Book
book2_instance = Book.objects.get(title= "1984", author= "George Orwell", publication_year= 1949)

# Expected Outcome

print(f"Author: {book2_instance.author}")
Author: George Orwell
print(f"Title: {book2_instance.title}")
Title: 1984
print(f"Publication Year: {book2_instance.publication_year}")
Publication Year: 1949

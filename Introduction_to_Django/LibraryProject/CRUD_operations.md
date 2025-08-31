# Create:

> > > from bookshelf.models import Book
> > > book2 = Book.objects.create(title= "1984", author= "George Orwell", publication_year= 1949)

> > > print(book2)
> > > Book object (2)
> > > print(book2.title)
> > > 1984
> > > print(book2.author)
> > > George Orwell
> > > print(book2.publication_year)
> > > 1949
> > > Book.objects.all().values()
> > > <QuerySet [{'id': 2, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]>

# Retrieve:

> > > from bookshelf.models import Book
> > > book2_instance = Book.objects.get(title= "1984", author= "George Orwell", publication_year= 1949)

> > > print(f"Author: {book2_instance.author}")
> > > Author: George Orwell
> > > print(f"Title: {book2_instance.title}")
> > > Title: 1984
> > > print(f"Publication Year: {book2_instance.publication_year}")
> > > Publication Year: 1949

# Update

> > > from bookshelf.models import Book
> > > book2_instance = Book.objects.get(title= "1984", author= "George Orwell", publication_year= 1949)

book2_instance.title= "Nineteen Eighty-Four"

> > > book2_instance.save()
> > > print(Book.objects.get(author= "George Orwell").title)
> > > Nineteen Eighty-Four
> > > print(f"Title: {book2_instance.title}")
> > > Title: Nineteen Eighty-Four

# Delete

> > > book2_instance.delete()
> > > (1, {'bookshelf.Book': 1})

> > > Book.objects.filter(author= "George Orwell").count()
> > > 0

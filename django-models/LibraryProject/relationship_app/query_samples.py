from .models import Book, Library, Librarian

Book.objects.filter(author_id=1).all()

library = Library.objects.get(name="LASU library")
library.books.all()

Librarian.objects.filter(library_id=1).all()
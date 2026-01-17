from .models import Book, Library, Librarian

Book.objects.filter(author_id=1).all()

library_name = "LASU Library"

library = Library.objects.get(name=library_name)
library.books.all()

Librarian.objects.filter(library_id=1).all()
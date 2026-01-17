from .models import Book, Library, Librarian, Author


author_name = "Wole Soyinka"
author = Author.objects.get(name=author_name)
Book.objects.filter(author=author).all()

library_name = "LASU Library"

library = Library.objects.get(name=library_name)
library.books.all()

Librarian.objects.get(library=library)
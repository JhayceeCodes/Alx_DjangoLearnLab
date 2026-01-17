from .models import Book, Library, Librarian

Book.objects.filter(author_id=1).all()

Book.objects.all()

Librarian.objects.filter(library_id=1).all()
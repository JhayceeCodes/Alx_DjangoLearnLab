from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book

#can_create --- users with this permission can add new books
@permission_required('book_shelf.can_create', raise_exception=True)
def create_book(request):
    ...


#can_list --- users with this permission can view books
@permission_required('book_shelf.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return HttpResponse({
        "books": books
    })


#can_edit --- users with this permission can edit book details
@permission_required('book_shelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    ...


#can_edit --- users with this permission can delete book with provided book id
@permission_required('book_shelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    ...

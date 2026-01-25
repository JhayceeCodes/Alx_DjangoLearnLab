from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

#can_create --- users with this permission can add new books
@permission_required('book_shelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
         form = ExampleForm(request.POST)
         if form.is_valid():
              title = form.cleaned_data["title"]
              author = form.cleaned_data["author"]
              publication_year = form.cleaned_data["publicaiton_year"]

              return HttpResponse("Book uploaded successfully")
    else:
         form = ExampleForm
    return render(request, 'bookshelf/form_example.html', {'form': form})


#can_list --- users with this permission can view books
@permission_required('book_shelf.can_view', raise_exception=True)
def book_list(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all() 
      context = {'books': books} 
      return render(request, 'relationship_app/list_books.html', context)



#can_edit --- users with this permission can edit book details
@permission_required('book_shelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    ...


#can_edit --- users with this permission can delete book with provided book id
@permission_required('book_shelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    ...

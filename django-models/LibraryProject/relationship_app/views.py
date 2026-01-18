from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Library, Book

def list_books(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all() 
      context = {'books': books} 
      return render(request, 'relationship_app/list_books.html', context)


class BookList(ListView):
      model = Library
      template_name = 'relationship_app/library_detail.html'

class LibraryDetailView(DetailView):
      model = Book


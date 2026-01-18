from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book

def book_list(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all() 
      context = {'books': books} 
      return render(request, 'list_books.html', context)


class BookList(ListView):
      ...

class BookDetail(DetailView):
      ...


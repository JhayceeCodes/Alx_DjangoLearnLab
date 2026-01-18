from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
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


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/signup.html'

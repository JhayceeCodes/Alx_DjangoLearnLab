from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) #Logs in the user automatically
            messages.success(request, "Registration Successful!")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page (e.g., a home or dashboard view)
                return redirect('home') 
            else:
                # Handle invalid login (though form.is_valid() usually catches this)
                pass 
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

def is_admin(user):
    return user.profile.role == "admin"

def is_librarian(user):
    return user.profile.role == "librarian"

def is_member(user):
    return user.profile.role == "member"

@user_passes_test(is_admin, login_url="/login")
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian, login_url="/login")
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member, login_url="/login")
def member_view(request):
    return render(request, "relationship_app/member_view.html")


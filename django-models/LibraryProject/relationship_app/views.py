from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from .forms import BookForm
from django.contrib.auth.decorators import permission_required, user_passes_test, login_required, permission_required
from .models import Library, Book


@login_required
def is_admin(user):
    return user.userprofile.role == 'Admin'
@login_required
def is_librarian(user):
    return user.userprofile.role == 'Librarian'
@login_required
def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


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





@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the list of books after saving
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# View to edit a book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect after editing
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

# View to delete a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect after deletion
    return render(request, 'relationship_app/delete_book.html', {'book': book})

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
import views
from .views import list_books, LibraryDetailView, SignUpView, login_view


urlpatterns =[
    path('books/', list_books),
    path('library_detail/', LibraryDetailView.as_view()),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='login'),
    path('signup/', views.register, name='signup'),
    path('books/add/', views.add_book, name="add_book/"),
    path('books/edit/<int:book_id>/', views.edit_book, name="edit_book/"),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'), 
]
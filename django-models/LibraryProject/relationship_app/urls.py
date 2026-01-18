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
]
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, SignUpView, login_view


urlpatterns =[
    path('books/', list_books),
    path('library_detail/', LibraryDetailView.as_view()),
    path('login/', login_view),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
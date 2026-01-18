from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns =[
    path('books/', list_books),
    path('library_detail/', LibraryDetailView.as_view())
]
from django.urls import path
from .views import BookCreateView, BookDestroyView, BookDetailView, BookListView

urlpatterns  = [
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/", BookCreateView.as_view(), name="book-create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/<int:pk>/", BookDestroyView.as_view(), name="book-delete")
]
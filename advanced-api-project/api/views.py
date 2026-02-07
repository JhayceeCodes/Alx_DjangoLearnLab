from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import BookSerializer
from .models import Book

class BookListView(ListAPIView):
    """Return a list of all books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    


class BookDetailView(RetrieveAPIView):
    """Return details of a single book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(CreateAPIView):
    """Allow authenticated users to create a book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(UpdateAPIView):
    """Allow authenticated users to update a book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(DestroyAPIView):
    """Allow authenticated users to delete a book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
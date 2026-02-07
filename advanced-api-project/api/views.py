from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import BookSerializer
from .models import Book

class BookListView(ListAPIView):
    """Return a list of all books."""
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    search_fields = ["title", "author"]
    ordering_fields = ["title", "publication_year"]
    ordering = ["-publication_year"]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    

class BookDetailView(RetrieveAPIView):
    """Return details of a single book."""
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(CreateAPIView):
    """Allow authenticated users to create a book."""
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    


class BookUpdateView(UpdateAPIView):
    """Allow authenticated users to update a book."""
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    


class BookDeleteView(DestroyAPIView):
    """Allow authenticated users to delete a book."""
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
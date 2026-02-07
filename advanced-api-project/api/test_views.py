from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Book

User = get_user_model()


class TestBookView(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020
        )

    def test_book_list(self):
        url = reverse("book-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_book_delete_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        url = reverse("book-delete", args=[self.book.id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_book_delete_unauthenticated(self):
        url = reverse("book-delete", args=[self.book.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

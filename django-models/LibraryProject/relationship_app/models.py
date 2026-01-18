from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("librarian", "Librarian"),
        ("member", "Member")
    ]
    user = models.OneToOneField(User)
    role = models.CharField(choices=ROLE_CHOICES, default="member")

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Library(models.Model):
    books = models.ManyToManyField(Book)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



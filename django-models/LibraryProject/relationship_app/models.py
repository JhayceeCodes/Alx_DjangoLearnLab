from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=20)

class Library(models.Model):
    books = models.ManyToManyField(Book)
    name = models.CharField(max_length=20)

class Librarian(models.Model):
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)



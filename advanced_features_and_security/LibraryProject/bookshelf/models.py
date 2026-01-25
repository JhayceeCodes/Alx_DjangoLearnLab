from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True)
    profile_photo = models.ImageField(null=True, blank=True)

class CustomUserManager(UserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not extra_fields.get("date_of_birth"):
            raise ValueError("Please enter date of birth")
        
        return super().create_user(username, email, password, **extra_fields)
        
    def create_superuser(self, username, email, password, **extra_fields):
        if not extra_fields.get("date_of_birth"):
            raise ValueError("Please enter date of birth")
        return super().create_superuser(username, email, password, **extra_fields)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view", "Can view"),
            ("can_create", "Can create"),
            ("can_edit", "Can edit"),
            ("can_delete", "Can delete")
        ]
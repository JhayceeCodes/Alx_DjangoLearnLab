from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='images/profile')
    followers = models.ManyToManyField('self', symmetrical=False)
    

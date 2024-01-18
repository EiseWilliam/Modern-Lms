from django.db import models

# Create your models here.
# users/models.py
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # Add any other fields you want for the user profile

    def __str__(self):
        return self.user.username

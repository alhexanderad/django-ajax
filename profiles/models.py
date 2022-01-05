from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField()
  avatar = models.ImageField(default='avatar.png',upload_to='avatars')
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  class Meta:
    """Meta definition for Profile."""

    verbose_name = 'Profile'
    verbose_name_plural = 'Profiles'

  def __str__(self):
    return f"profile of the user {self.user.username}"


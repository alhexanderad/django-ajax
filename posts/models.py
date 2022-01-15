from email.mime import image
from pyexpat import model
from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.contrib.auth.models import User
from profiles.models import Profile
class Post(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  liked = models.ManyToManyField(User, blank=True)
  author = models.ForeignKey(Profile, on_delete=models.CASCADE)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  class Meta:
    """Meta definition for Post."""
    ordering = ('-created',)
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'

  def get_photos(self):
    return self.photo_set.all()

  def __str__(self):
    return str(self.title)
  
  @property
  def like_count(self):
    return self.liked.all().count()
  
class Photo(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  image = models.ImageField(upload_to="photos")
  created = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
      return f"{self.post.title}-{self.pk}"
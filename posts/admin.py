import site
from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Post, Photo

admin.site.register(Post)
admin.site.register(Photo)

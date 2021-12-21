from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Post

admin.site.register(Post)


from django.shortcuts import render
from .models import Post
from django.core import serializers
from django.http import JsonResponse,HttpResponse
from .forms import PostForm
from profiles.models import Profile


def post_list_and_create(request):
  form = PostForm(request.POST or None)
  #qs = Post.objects.all()
  
  if request.is_ajax():
    if form.is_valid():
      author = Profile.objects.get(user=request.user)
      print(author)
      instance = form.save(commit=False)
      instance.author = author
      instance.save()
      return JsonResponse({
        'title': instance.title,
        'body': instance.body,
        'author': instance.author.user.username,
        'id':instance.id,
      })

    
  context = {
    #'qs' :qs,
    'form':form
  }
  return render(request, 'posts/main.html',context)

def post_detail(request,pk):
  obj=Post.objects.get(pk=pk)
  form = PostForm()
  
  context ={
    'obj':obj,
    'form':form,
  }
  
  return render(request, 'posts/detail.html', context)
  
def load_post_data_view(request, num_posts):
  if request.is_ajax():
    visible = 3
    upper= num_posts
    lower = upper - visible
    size = Post.objects.all().count()
    
    print('Cantidad de posts',size)
    print('Cantidad de UPPER',upper)

    qs = Post.objects.all()
    
    data = []
    for obj in qs:
      item =  {
        'id' : obj.id,
        'title' : obj.title,
        'body' : obj.body,
        'liked': True if request.user in obj.liked.all() else False,
        'count': obj.like_count,
        'author' : obj.author.user.username
      }
      data.append(item)
    return JsonResponse({'data':data[lower:upper], 'size':size})

def like_unlike_post(request):
  if request.is_ajax():
    pk = request.POST.get('pk')
    print(pk)
    obj = Post.objects.get(pk= pk)
    if request.user in obj.liked.all():
      liked = False
      obj.liked.remove(request.user)
    else:
      liked = True
      obj.liked.add(request.user)
    return JsonResponse({'liked': liked, 'count': obj.like_count})

def hello_world_view(request):
  return JsonResponse({'text': 'Este mensaje es de la vista 2022'})
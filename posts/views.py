from json.encoder import JSONEncoder
from django.shortcuts import render
from .models import Post, Photo
from django.http import JsonResponse,HttpResponse
from .forms import PostForm
from profiles.models import Profile
from .utils import action_permission
from django.contrib.auth.decorators import login_required

@login_required
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

@login_required
def post_detail(request,pk):
  obj=Post.objects.get(pk=pk)
  print('post_detail',obj)
  form = PostForm()
  
  context ={
    'obj':obj,
    'form':form,
  }
  
  return render(request, 'posts/detail.html', context)
  
@login_required
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

@login_required
def post_detail_data_view(request, pk):
  obj= Post.objects.get(pk=pk)
  data = {
    'id': obj.id,
    'title': obj.title,
    'body': obj.body,
    'author': obj.author.user.username,
    'logged_in': request.user.username,
  }
  return JsonResponse({'data':data})

@login_required
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

@action_permission
@login_required
def update_post(request, pk):
  obj = Post.objects.get(pk=pk)
  if request.is_ajax():
    new_title = request.POST.get('title')
    new_body = request.POST.get('body')
    obj.title = new_title
    obj.body = new_body
    obj.save()
    return JsonResponse({
      'title':new_title,
      'body': new_body,
    })

@login_required
@action_permission
def delete_post(request,pk):
  obj = Post.objects.get(pk=pk)
  if request.is_ajax():
    obj.delete()
    return JsonResponse({'msg':'some message'})
  return JsonResponse({'msg':'acceso denegado - debe de ingresar por ajax '})
  
@login_required
@action_permission
def image_upload_view(request):
  if request.method == 'POST':
    img = request.FILES.get('file')
    new_post_id = request.POST.get('new_post_id')
    post_id = Post.objects.get(pk = new_post_id)
    Photo.objects.  create(post=post_id, image=img)
    
    print("ID de post",post_id)
    print("new post id", new_post_id)
  return HttpResponse()
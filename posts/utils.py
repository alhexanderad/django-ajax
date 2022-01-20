from .models import Post
from profiles.models import Profile
from django.http import HttpResponse

def action_permission(func):
  def wrapper(request, **kwargs):
    pk = kwargs.get('pk')
    print("Se mostra de la vista kwargs",pk)
    print ("De los usuariios de request.use", type(request.user))
    if request.user.is_authenticated:
      profile = Profile.objects.get(user=request.user)
      post= Post.objects.get(pk=pk)
      if profile.user == post.author.user:
        print('yes')
        return func(request, **kwargs)
      else:
        print('no')
        return HttpResponse('acceso denegado - necesitas ser autor del post para poder borrar')
    else:
      return HttpResponse('acceso denegado - deber serr un usuario')
  return wrapper
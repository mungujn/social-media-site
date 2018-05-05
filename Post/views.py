from django.shortcuts import render

# Create your views here.
from Post.forms import PostForm
from Post.models import Post


def posts(request):
    template_name = 'Post/posts.html'
    #posts
    try:
        posts = Post.objects.all()[:10]
    except AttributeError:
        posts = None
    return render(request, template_name, {'posts':posts,'type':None})

def post(request):
    template_name = 'Post/posts.html'
    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
    else:
        post_form = PostForm()

    return render(request, template_name, {'form': post_form,'var': None})

from django.shortcuts import render
from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
    data = Post.objects.all()
    return render(request, 'post_list.html', {"context":data})


def post_detail(request, id_post):
    data = Post.objects.get(id = id_post)
    return render(request,'post_detail.html', {'context':data})


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()    
    return render (request,'new_post.html', {'form': form} )

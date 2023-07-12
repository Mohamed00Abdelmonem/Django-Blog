from django.shortcuts import render
from .models import Post
# Create your views here.

def post_list(request):
    data = Post.objects.all()
    return render(request, 'post_list.html', {"context":data})


def post_detail(request, id_post):
    data = Post.objects.get(id = id_post)
    return render(request,'post_detail.html', {'context':data})
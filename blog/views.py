from django.shortcuts import render, redirect
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
            myform = form.save(commit=False)
            myform.auther = request.user
            myform.save()
            return redirect('/')
    else:
        form = PostForm()    
    return render (request,'new_post.html', {'form': form} )

def edit_post(request, id_post):
    data = Post.objects.get(id = id_post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.auther = request.user
            myform.save()
            return redirect('/')
    else:
        form = PostForm(instance=data)    
    return render (request,'edit_post.html', {'form': form} )



def delete_post(request, id_post):
    data = Post.objects.get(id = id_post)
    data.delete()
    return redirect('/')


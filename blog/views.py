from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

def post_list(request): # query , template : context
    data = Post.objects.all()
    return render(request, 'post_list.html', {"context":data})


class PostList(ListView): # template : post_list  name database & _ & List or detail or update or delete
    model = Post          # post_list , object_list 


def post_detail(request, id_post):
    data = Post.objects.get(id = id_post)
    return render(request,'post_detail.html', {'context':data})

class PostDetail(DetailView):
    model = Post

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
class PostCreate(CreateView):
    model = Post
    fields = ['title','content', 'create_date', 'draft', 'tags', 'image', 'auther']
    success_url = '/'



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


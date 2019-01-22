from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'ftest/index.html', {'posts':posts})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/ftest/')
    else:
        form = PostForm()
    return render(request, 'ftest/create.html', {'form': form})

def delpost(request, postid = None):
    post = get_object_or_404(Post, pk = postid)
    post.delete()
    return HttpResponseRedirect(reverse('ftest:index'))

def editpost(request, postid = None):
    post = get_object_or_404(Post, pk = postid)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('ftest:index'))
    else:
        form = PostForm(instance = post)
        return render(request, 'ftest/postedit.html', {'form': form, 'postid': postid})



from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, "blog/indexForBlog.html", {"posts": posts})

def create(request):
    if request.method == "POST":
        post = Post()
        post.author = request.POST.get("author")
        post.title = request.POST.get("title")
        post.text = request.POST.get("text")
        post.created_date = request.POST.get("created_date")
        post.published_date = request.POST.get("published_date")
        post.save()
        return HttpResponseRedirect("/")

def edit(request, id):
    try:
        post = Post.objects.get(id=id)

        if request.method == "POST":
            post.author = request.POST.get("author")
            post.title = request.POST.get("title")
            post.text = request.POST.get("text")
            post.created_date = request.POST.get("created_date")
            post.published_date = request.POST.get("published_date")
            post.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "blog/edit.html", {"post": post})
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Post not found</h2>")


def delete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return HttpResponseRedirect("/")
    except post.DoesNotExist:
        return HttpResponseNotFound("<h2>Post not found</h2>")


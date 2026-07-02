from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from .forms import PostForm


# Home Page (List all posts)
def home(request):
    posts = Post.objects.all().order_by("-created_at")

    return render(
        request,
        "blog/home.html",
        {"posts": posts},
    )


# Detail Page
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(
        request,
        "blog/detail.html",
        {"post": post},
    )


# Create Post
def create(request):

    if request.method == "POST":

        form = PostForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("home")

    else:
        form = PostForm()

    return render(
        request,
        "blog/create.html",
        {"form": form},
    )


# Update Post
def update(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":

        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()

            return redirect("detail", pk=pk)

    else:
        form = PostForm(instance=post)

    return render(
        request,
        "blog/update.html",
        {
            "form": form,
            "post": post,
        },
    )


# Delete Post
def delete(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()

        return redirect("home")

    return render(
        request,
        "blog/delete.html",
        {"post": post},
    )
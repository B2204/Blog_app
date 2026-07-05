from django.shortcuts import render, redirect, get_object_or_404
from django.core.cache import cache

from .models import Post
from .forms import PostForm
from .tasks import send_welcome_email


# Home Page
def home(request):

    # Try to get posts from Redis
    posts = cache.get("posts")

    # Cache Miss
    if posts is None:
        print("Loading posts from database...")
        posts = Post.objects.select_related("author").all()

        # Store in Redis for 60 seconds
        cache.set("posts", posts, timeout=60)

    return render(
        request,
        "blog/home.html",
        {
            "posts": posts,
        },
    )
posts = cache.get("posts")

# Detail Page
def detail(request, pk):

    post = get_object_or_404(
        Post.objects.select_related("author"),
        pk=pk,
    )

    return render(
        request,
        "blog/detail.html",
        {
            "post": post,
        },
    )


# Create Post
def create_post(request):

    if request.method == "POST":

        form = PostForm(request.POST)

        if form.is_valid():

            post = form.save()

            # Delete cache
            cache.delete("posts")

            # Background Task
            if post.author and hasattr(post.author, "email"):
                send_welcome_email.delay(post.author.email)

            return redirect("home")

    else:

        form = PostForm()

    return render(
        request,
        "blog/create.html",
        {
            "form": form,
        },
    )


# Update Post
def update(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":

        form = PostForm(
            request.POST,
            instance=post,
        )

        if form.is_valid():

            post = form.save()

            # Delete cache
            cache.delete("posts")

            # Optional Background Task
            if post.author and hasattr(post.author, "email"):
                send_welcome_email.delay(post.author.email)

            return redirect(
                "detail",
                pk=pk,
            )

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

        # Delete cache
        cache.delete("posts")

        return redirect("home")

    return render(
        request,
        "blog/delete.html",
        {
            "post": post,
        },
    )
from django.shortcuts import render, get_object_or_404
from .models import Blog


def blogposts(request):
    blogs = Blog.objects
    return render(request, 'blog/blogposts.html', {'blogs': blogs})


def blog_post(request, blog_id):
    blog_post_item = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_post.html', {'blog': blog_post_item})

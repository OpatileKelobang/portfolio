from django.shortcuts import render


def blogposts(request):
    return render(request, 'blog/blogposts.html')

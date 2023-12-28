# Create your views here.
from django.shortcuts import render

from APP_BLOG.models import Post
from taggit.models import Tag


def index(request):
    return render(request, "APP_BLOG/index.html")

def blog(request):
    context = {
        'blog': Post.objects.all(),
    }
    return render(request, 'APP_BLOG/blog.html', context)

def post(request, slug):
    context = {
        'post': Post.objects.get(slug=slug),
    }
    return render(request, 'APP_BLOG/post.html', context)

def tag(request, tag):
    context = {
        'posts': Post.objects.filter(tags__name__in=[tag]),
    }
    return render(request, 'APP_BLOG/tag.html', context)
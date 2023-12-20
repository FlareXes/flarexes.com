# Create your views here.
from django.shortcuts import render

from APP_BLOG.models import Post


def index(request):
    return render(request, "APP_BLOG/index.html")


def post(request, slug):
    context = {
        'post': Post.objects.get(slug=slug),
    }
    return render(request, 'APP_BLOG/post.html', context)

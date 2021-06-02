from django.shortcuts import render
from .models import Post

def article_page(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "articles/articles.html", context)

def post_page(request, post_id):
    context = {
        'post': Post.objects.get(id=post_id)
    }
    return render(request, "articles/post.html", context)

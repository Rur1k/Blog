from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

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

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            save_author = form.save(commit=False)
            save_author.author = request.user
            save_author.save()
            return redirect('articles')

    form = PostForm()

    data = {
        'form': form,
    }

    return render(request, "articles/new_post.html", data)

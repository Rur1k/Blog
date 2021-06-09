from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.views.generic import DetailView, UpdateView, DeleteView

class PostUpdateView(UpdateView):
    model = Post
    success_url = '/editdone/'
    template_name = 'articles/new_post.html'

    form_class = PostForm

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/deletedone/'
    template_name = 'articles/post_delete.html'

def article_page(request):
    context = {
        'posts': Post.objects.filter(status=2).order_by('-post_data')
    }
    return render(request, "articles/articles.html", context)

def new_article_page(request):
    context = {
        'posts': Post.objects.filter(status=2).order_by('-post_data')[:2]
    }
    return render(request, "articles/newarticles.html", context)

def admin_article_page(request):
    context = {
        'all_posts': Post.objects.all().order_by('-post_data')
    }
    return render(request, "articles/admin_panel.html", context)

def user_article_page(request):
    context = {
        'user_posts': Post.objects.filter(author=request.user).order_by('-post_data')
    }
    return render(request, "articles/userpanel.html", context)

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
            return redirect('newpostdone')

    form = PostForm()

    data = {
        'form': form,
    }
    return render(request, "articles/new_post.html", data)

def new_post_done(request):
    return render(request, 'articles/newpostdone.html')

def edit_done(request):
    return render(request, 'articles/editdone.html')

def delete_done(request):
    return render(request, 'articles/deletedone.html')


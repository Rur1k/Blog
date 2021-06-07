from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField('Название котегории', max_length=64)

    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField('Заголовок статьи', max_length=64)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    announcement_post = models.CharField('Анонс статьи', max_length=255, null=True)
    text = models.TextField('Текст статьи')
    post_data = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField('Имя комментатора', max_length=16)
    comment_text = models.CharField('Текст комментария', max_length=255)

    def __str__(self):
        return self.author_name

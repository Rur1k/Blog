import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField('Название статьи', max_length = 255)
    text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации статьи')


    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Имя комментатора', max_length = 16)
    comment_text = models.CharField('Текст комментария', max_length = 255)

    def __str__(self):
        return self.author_name
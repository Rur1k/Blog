from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_page, name='articles'),
    path('post/<int:post_id>', views.post_page, name='post'),
]
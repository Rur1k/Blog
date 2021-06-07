from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.article_page, name='articles'),
    path('post/<int:post_id>', views.post_page, name='post'),
    path('new_post/', views.new_post, name='new_post'),
]
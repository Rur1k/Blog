from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.article_page, name='articles'),
    path('newarticles/', views.new_article_page, name='newarticles'),
    path('post/<int:post_id>', views.post_page, name='post'),
    path('new_post/', views.new_post, name='new_post'),
    path('adminpanel/', views.admin_article_page, name='adminpanel'),
    path('userpanel/', views.user_article_page, name='userpanel'),
    path('edit/<int:pk>', views.PostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', views.PostDeleteView.as_view(), name='delete'),
    path('newpostdone/', views.new_post_done, name='newpostdone'),
    path('editdone/', views.edit_done, name='editdone'),
]
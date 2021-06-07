from django.conf.urls import url
from . import views

urlpatterns = [
    url('register/', views.register, name='register'),
    url('login/', views.user_login, name='login'),
    url('logout/', views.user_logout, name='logout'),
    url('', views.dashboard, name='dashboard'),
]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogposts, name='blogposts'),
    path('<int:blog_id>/', views.blog_post, name='blog_post'),

]

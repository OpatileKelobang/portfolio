from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogposts, name='blogposts'),

]

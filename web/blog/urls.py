from django.views.generic import ListView, DetailView
from django.urls import path, include
from blog.models import Post

urlpatterns = [
    path(r'', ListView.as_view(queryset=Post.objects.order_by("-date")[:25],
                              template_name="blog/blog.html"))
]

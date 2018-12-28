from django.views.generic import ListView, DetailView
from django.conf.urls import url, include
from . import views
from webapp.models import Post, WarePost, FAQPost

urlpatterns = [
    url(r'^contacts/$', views.contacts, name='contacts'),

    url(r'^$', ListView.as_view(queryset=Post.objects.order_by("-date")[:25],
                                template_name="webapp/index.html")),

    url(r'^ware/$', ListView.as_view(queryset=WarePost.objects.order_by("-date")[:25],
                                template_name="webapp/ware.html")),

    url(r'^services/$', ListView.as_view(queryset=WarePost.objects.order_by("-date")[:25],
                                template_name="webapp/services.html")),

    url(r'^faq/$', ListView.as_view(queryset=FAQPost.objects.order_by("-date")[:25],
                                template_name="webapp/faq.html"))
]

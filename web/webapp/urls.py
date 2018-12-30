from django.views.generic import ListView, DetailView
from django.conf.urls import url, include
from . import views
from webapp.models import WarePost, FAQPost, ServicesPost

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^contacts/$', views.contacts, name='contacts'),

    url(r'^ware/$', ListView.as_view(queryset=WarePost.objects.order_by("-date")[:25],
                                template_name="webapp/ware.html")),

    url(r'^services/$', ListView.as_view(queryset=ServicesPost.objects.order_by("-date")[:25],
                                template_name="webapp/services.html")),

    url(r'^faq/$', ListView.as_view(queryset=FAQPost.objects.order_by("-date")[:25],
                                template_name="webapp/faq.html"))
]

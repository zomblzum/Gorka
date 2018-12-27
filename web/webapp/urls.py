from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ware/$', views.ware, name='ware'),
    url(r'^services/$', views.services, name='services'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    # url(r'^about/$', views.about, name='about')
]

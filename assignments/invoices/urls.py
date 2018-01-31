from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.invoices, name='invoices'),
    url(r'^(?P<id>[0-9]+)/$', views.invoices, name='invoices'),
    url(r'^(?P<id>[0-9]+)$', views.invoices, name='invoices'),
]

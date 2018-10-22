from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_product, name='list_products'),
    url(r'^new', views.create_product, name='create_product'),
    url(r'^update/(?P<id>[0-9]+)$', views.update_product, name="update_product"),
    url(r'^delete/(?P<id>[0-9]+)$', views.delete_product, name="delete_product"),
    ]
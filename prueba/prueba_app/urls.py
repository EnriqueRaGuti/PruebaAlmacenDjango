from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^producto$', views.ProductoList.as_view()),
    url(r'^producto/(?P<pk>[0-9]+)$', views.ProductoDetail.as_view()),
    # url(r'^producto/$', views.ProductoDetail.as_view()),
]
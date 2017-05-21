from django.conf.urls import url

from . import views

urlpatterns = [
    url('^input/$', views.input, name='input'),
    url(r'^complete/$', views.complete, name='complete'),
    url(r'^complete/(\d+)/$', views.complete, name='complete_by_id'),
]
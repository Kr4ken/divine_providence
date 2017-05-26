from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^interests/$', views.getInterests, name='getInrerests'),
    url(r'^interests/(?P<key>.+)/$', views.completeInterest, name='getInrerests'),
]
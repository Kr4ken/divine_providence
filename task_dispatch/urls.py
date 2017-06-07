from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^interests/$', views.getInterests, name='getInrerests'),
    url(r'^interests/(?P<key>.+)/$', views.completeInterest, name='getInrerests'),
    url(r'^control/id/sync/$',views.sync_ids,name="Sync_Ids"),
    url(r'^control/int/sync/$',views.sync_interests,name="Sync_Interests")
	# url(r'^control/(?p<command>.+)/$',views.comm)
]
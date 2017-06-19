from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^interests/$', views.getInterests, name='getInrerests'),
    # url(r'^tasks/input/$', views.getInputTasks, name='getInputTasks'),
    url(r'^tasks/input/((?P<key>.+)/)?$', views.inputTasks, name='InputTasks'),
    url(r'^interests/(?P<key>.+)/$', views.completeInterest, name='getInrerests'),
    url(r'^control/id/sync/$',views.sync_ids,name="Sync_Ids"),
    url(r'^control/int/sync/$',views.sync_interests,name="Sync_Interests"),
    url(r'^control/input/sync/$',views.sync_input_tasks,name="Sync_Input_Tasks")
	# url(r'^control/(?p<command>.+)/$',views.comm)
]
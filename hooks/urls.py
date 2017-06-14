from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^trello/$', views.trello_hook, name='trello_hook'),
	url(r'^habatica/$', views.habatica_hook, name='habatica_hook'),
	# url(r'^control/(?p<command>.+)/$',views.comm)
]

import os

from django.conf import settings
from django.views.generic import TemplateView

from .controller.trello_wrapper import TrelloWrapper

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import InterestSerializer, TaskSerializer

tw = TrelloWrapper()

@csrf_exempt
def getInputTasks(request):
    if request.method == 'GET':
        tasks = tw.get_input_tasks()
        serializer = TaskSerializer(tasks,many=True)
        return JsonResponse(serializer.data,safe=False)


@csrf_exempt
def getInterests(request):
    if request.method == 'GET':
        # interests = tc.get_interest_list()
        interests = tw.get_interests()
        serializer = InterestSerializer(interests,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def getInterest(request, key):
    if request.method == 'GET':
        interests = tc.get_interest_list()
        serializer = InterestSerializer(interests, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def completeInterest(request, key):
    if request.method == 'DELETE':
        # interest = tc.complete_interest(key)
        interest = tw.complete_interest(key)
        serializer = InterestSerializer(interest, many=False)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'GET':
        interest = tc.get_interest(key)
        serializer = InterestSerializer(interest, many=False)
        return JsonResponse(serializer.data, safe=False)

    return HttpResponse(status=404)

@csrf_exempt
def sync_ids(request):
	if request.method == 'POST':
		return HttpResponse(status=200, content=tw.fill_all())
		# return JsonResponse("{'message':'"+tc.fill_all()+"'}")

@csrf_exempt
def sync_interests(request):
    if request.method == 'POST':
        return HttpResponse(status=200, content=tw.fill_interests())

@csrf_exempt
def sync_input_tasks(request):
    if request.method == 'POST':
        return HttpResponse(status=200, content=tw.fill_input_tasks())



class AngularApp(TemplateView):

   template_name = 'task_dispatch/index.html'

   def get_context_data(self, **kwargs):
        context = super(AngularApp, self).get_context_data(**kwargs)
        context['ANGULAR_URL'] = settings.ANGULAR_URL
        return context


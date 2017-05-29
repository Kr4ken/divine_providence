import os

from django.conf import settings
from django.views.generic import TemplateView

from .controller.trello.trello_controller import TrelloController

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .controller.trello.interest import Interest
from .serializers import InterestSerializer

tc = TrelloController(os.path.join(settings.BASE_DIR, "config.json"))

@csrf_exempt
def getInterests(request):
    if request.method == 'GET':
        interests = tc.get_interest_list()
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
        interest = tc.complete_interest(key)
        serializer = InterestSerializer(interest, many=False)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'GET':
        interest = tc.get_interest(key)
        serializer = InterestSerializer(interest, many=False)
        return JsonResponse(serializer.data, safe=False)

    return HttpResponse(status=404)



class AngularApp(TemplateView):

   template_name = 'task_dispatch/index.html'

   def get_context_data(self, **kwargs):
        context = super(AngularApp, self).get_context_data(**kwargs)
        context['ANGULAR_URL'] = settings.ANGULAR_URL
        return context


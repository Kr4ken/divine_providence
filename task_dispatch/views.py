from django.shortcuts import render
from django.http import HttpResponse
import os

from .models import *
from .controller.trello_controller import trello_controller
from django.conf import settings
from django.views.generic import View,TemplateView

# Create your views here.
def input(request):
    current_task = Task.objects.get(pk=1)
    context ={ 'task' : current_task,
               'task_types':Task_type.objects.all(),
               'types': Type.objects.all()}
    return render(request,'task_dispatch/input.html',context)

def complete(request,index = None):
    tc = trello_controller(os.path.join(settings.BASE_DIR,"config.json"))
    new_item = None
    elems = tc.get_interest_list()
    if not index is None:
        new_item = tc.get_new_item_interst_list(int(index))

    context ={ 'elems': elems,
               'new_item':new_item}
    return render(request,'task_dispatch/complete.html',context)


class AngularApp(TemplateView):

   template_name = 'task_dispatch/index.html'

   def get_context_data(self, **kwargs):
        context = super(AngularApp, self).get_context_data(**kwargs)
        context['ANGULAR_URL'] = settings.ANGULAR_URL
        return context

class SampleView(View):
    def get(self, request):
        return render(request,"OK!")
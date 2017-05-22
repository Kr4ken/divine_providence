from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .controller.trello_controller import trello_controller
from django.conf import settings
import os

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

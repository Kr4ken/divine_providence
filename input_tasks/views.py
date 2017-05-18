from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
    current_task = Task.objects.get(pk=1)
    context ={ 'task' : current_task}
    return render(request,'input_tasks/index.html',context)
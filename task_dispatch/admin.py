from django.contrib import admin

# Register your models here.

from .models import Task, Task_type, Type, Urgency, IdObject

admin.site.register(Task_type)
admin.site.register(Task)
admin.site.register(Type)
admin.site.register(Urgency)
admin.site.register(IdObject)

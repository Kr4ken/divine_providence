from django.contrib import admin

# Register your models here.

from .models import Task, IdObject, Interest

admin.site.register(Task)
admin.site.register(IdObject)
admin.site.register(Interest)

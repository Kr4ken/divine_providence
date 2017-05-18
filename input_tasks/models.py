from django.db import models

# Create your models here.
class Task_type(models.Model):
	ident = models.CharField(max_length=20)
	description = models.CharField(max_length=200)

	def __str__(self):
		return self.description

class Urgency(models.Model):
	ident = models.CharField(max_length=20)
	description = models.CharField(max_length=200)
	def __str__(self):
		return self.description

class Type(models.Model):
	ident = models.CharField(max_length=20)
	description = models.CharField(max_length=200)
	def __str__(self):
		return self.description

class Task(models.Model):
	task_type = models.ForeignKey(Task_type)
	ident = models.CharField(max_length=40)
	urgency = models.ForeignKey(Urgency)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=2000)
	special = models.CharField(max_length=300)
	type = models.ForeignKey(Type)
	due_date=models.DateField()
	checklist=models.CharField(max_length=200)
	labels=models.CharField(max_length=200)
	sub_task=models.CharField(max_length=40)
	atribute=models.CharField(max_length=10)
	difficult=models.CharField(max_length=10)

	def __str__(self):
		return self.name


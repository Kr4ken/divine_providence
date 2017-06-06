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


class IdObject(models.Model):
	CARD_TYPE=0
	LIST_TYPE=1
	BOARD_TYPE=2
	LABEL_TYPE=3
	OBJECT_TYPES = (
		(CARD_TYPE, 'Card'),
		# ('Card', 0),
		(LIST_TYPE, 'List'),
		# ('List', 1),
		(BOARD_TYPE, 'Board'),
		# ('Board', 2),
		(LABEL_TYPE, 'Label')
		# ('Label', 3)
	)
	name = models.CharField(max_length=100,null=True)
	key = models.CharField(max_length=30)
	owner_key = models.CharField(max_length=30, default=None, null=True)
	type = models.IntegerField(choices=OBJECT_TYPES)

	def __str__(self):
		msgType=''
		if self.type==0:
			msgType='Карточка'
		elif self.type==1:
			msgType='Список'
		elif self.type==2:
			msgType='Доска'
		elif self.type==3:
			msgType='Ярлык'
		return msgType  +" : " +  self.name

class Interest(models.Model):
		key = models.CharField(max_length=30)
		name = models.CharField(max_length=100, null=True)
		img = models.CharField(max_length=200, null=True)
		list_key = models.CharField(max_length=30, null=True)
		description = models.CharField(max_length=300, null=True)
		pos = models.IntegerField


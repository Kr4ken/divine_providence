from django.db import models

# Create your models here.

class Task(models.Model):
	key = models.CharField(max_length=30)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500, null=True)
	duration = models.IntegerField(null=True)
	# type
	list_key = models.CharField(max_length=30)
	checklist = models.CharField(max_length=5000, null=True)
	due_date = models.DateTimeField(null=True)
	attribute = models.CharField(max_length=1, null=True)
	labels = models.CharField(max_length=2, null=True)
	special = models.CharField(max_length=1000, null=True)
	image = models.CharField(max_length=1000, null=True)

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
		list_name = models.CharField(max_length=100, null=True)
		description = models.CharField(max_length=300, null=True)
		ord_pos = models.IntegerField(null=True)

class TaskType(models.Model):
	key = models.CharField(max_length=30)
	name = models.CharField(max_length=200)

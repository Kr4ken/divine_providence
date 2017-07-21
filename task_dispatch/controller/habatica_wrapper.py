from task_dispatch.controller.habatica.habaticaclient import HabaticaClient
import json
from .trello.trello_controller import TrelloController
from ..models import Interest, Task, TaskType
from .trello.IdController import IdController
from django.db.models import Q
from django.conf import settings

class HabaticaWrapper:
	conf = json.load(open(settings.CONFIG_PATH, 'r', encoding="utf-8"))

	def task_to_habatica_task(self,task):
		task_type = 'todo'
		if (task.list_key == IdController.get_list_id('Привычки')):
			task_type = 'habit'
		elif (task.list_key == IdController.get_list_id('Каждый день')):
			task_type = 'daily'
		return {
		"alias" : task.key,
		"text" : task.name,
		"notes" : task.description,
		"type" : task_type
		}

	def sync_tasks(self, tasks):
		client = HabaticaClient(api_key = self.conf['habatica']['api_key'],
		                             api_token = self.conf['habatica']['token'])
		user = client.get_user()
		for task in tasks:
			user.sync_task(self.task_to_habatica_task(task))
		id_list = [x.key for x in tasks]
		for task in user.tasklist:
			if task.alias not in id_list:
				user.delete_task(task)

	def trello_sync(self):
		checked_list = Task.objects.filter(
			Q(list_key = IdController.get_list_id('Список покупок')) |
			Q(list_key = IdController.get_list_id('Личное')) |
			Q(list_key = IdController.get_list_id('Организационное')) |
			Q(list_key = IdController.get_list_id('Учеба/Работа')) |
			Q(list_key = IdController.get_list_id('Каждый день')) |
			Q(list_key = IdController.get_list_id('Привычки'))
		)
		self.sync_tasks(checked_list)
		return 'All OK!'




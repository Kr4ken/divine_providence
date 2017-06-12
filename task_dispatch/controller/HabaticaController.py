from task_dispatch.controller.habatica.habaticaclient import HabaticaClient
import json
from .trello.trello_controller import TrelloController

class HabaticaController:

	def __init__(self, config='config.json'):
		conf = json.load(open(config, 'r'))
		self.client = HabaticaClient(api_key = conf['habatica']['api_key'],
										api_token = conf['habatica']['token'])
		self.user = self.client.get_user()
		self.tc = TrelloController()
		self._checked_list_id = [
			ListId.PPersonal,
			ListId.POrgan,
			ListId.PWork,
			ListId.PEveryDay,
			ListId.PHabits
		]

	def add_task(self, task):
		self.user.add_task(task)

	def del_task(self,task):
		self.user.delete_task(task)

	def sync_task(self, task):
		# self.user.sync_task(task)
		task_model = task.get_habatica_model()
		# Если данная задача уже существует
		exist_task = self.user.get_task_alias_id(task_model['alias'])
		if not exist_task is None:
			# Если задача изменила свой тип
			if exist_task.type != task_model['type']:
				self.user.delete_task(exist_task)
				self.user.add_task(task_model)
			else:
				if exist_task.type == 'todo':
				# Пока обновление заменил на удаление и вставку
					self.user.delete_task(exist_task)
					self.user.add_task(task_model)
				else:
					self.user.update_task(task_model)
		else:
			self.add_task(task_model)

	def sync_tasks(self, tasks):
		for task in tasks:
			self.user.sync_task(task)
		id_list = [x.id for x in tasks]
		for task in self.user.tasklist:
			if task.alias not in id_list:
				self.user.delete_task(task)

	def trello_sync(self):
		checked_list = self.tc.get_task_model_list(ListId.PPersonal)\
					+ self.tc.get_task_model_list(ListId.POrgan) \
					+ self.tc.get_task_model_list(ListId.PWork) \
					+ self.tc.get_task_model_list(ListId.PEveryDay) \
					+ self.tc.get_task_model_list(ListId.PHabits)
		self.sync_tasks(checked_list)

	def handle_hook(self, handle_obj):
		json_obj = json.loads(handle_obj)
		# Если карточка удалена
		if  ('closed' in json_obj['action']['data']['card'] and  json_obj['action']['data']['card']['closed']):
			self.user.delete_task_by_id(json_obj['action']['data']['card']['id'])
		else:
			card = self.tc.client.get_card(json_obj['action']['data']['card']['id'])
			if card.list_id in self._checked_list_id:
				self.sync_task(TaskModel(card))
			# Тест удаления карточки которая переносится в другой список
			else:
				self.user.delete_task_by_id(json_obj['action']['data']['card']['id'])




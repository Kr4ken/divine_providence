import json
import random
from trello import TrelloClient
from ..models import Interest, Task
from django.conf import settings
from .trello.IdController import IdController


class TrelloWrapper:
	conf = json.load(open(settings.CONFIG_PATH, 'r', encoding="utf-8"))

	def fill_interests(self):
		Interest.objects.all().delete()
		print('Start fill interest')
		client = TrelloClient(
			api_key=self.conf['trello']['api_key'],
			token=self.conf['trello']['token'])
		print('connected')
		interestIgnoredList = self.conf['app']['intersest']['ignoredList']
		board_id = IdController.get_board_id('Интересы')
		l_board = client.get_board(board_id=board_id)
		l_lists = l_board.all_lists()
		print('start cycle')
		for l in l_lists:
			if l.name not in interestIgnoredList:
				counter = 0
				print('get cards for ' + l.name)
				for card in l.list_cards():
					print(card.name + ' performed')
					card.fetch_attachments(force=True)
					attach=None
					if card.get_attachments().__len__() > 0:
						attach = card.get_attachments()[0].url
					interest = Interest(key=card.id, name=card.name, img=attach, list_key=l.id,list_name=l.name , description=card.desc,ord_pos=counter)
					interest.save()
					counter= counter + 1
				print(l.name + ' list ended')
		return 'All OK'

	def fill_all(self, add_cards=False):
		print('start filling')
		client = TrelloClient(
			api_key=self.conf['trello']['api_key'],
			token=self.conf['trello']['token'])
		IdController.clear()
		board_list=[]
		for board in client.list_boards():
			list_list=[]
			b={}
			b['name'] = board.name
			b['key'] = board.id
			board_list.append(b)
			print('board_added'+board.name)
			for list in board.list_lists():
				card_list=[]
				l={}
				l['name'] = list.name
				l['key'] = list.id
				l['owner_key'] = board.id
				list_list.append(l)
				print('list_added' + list.name)
				if add_cards:
					for card in list.list_cards():
						c={}
						c['name'] = card.name
						c['key'] = card.id
						c['owner_key'] = list.id
						card_list.append(c)
						print('card added')
					IdController.fill_cards(card_list)
			for label in board.get_labels():
					print('label_added:' + label.name)
					IdController.fill_label({'name': label.name, 'key': label.id, 'owner_key': board.id})
			IdController.fill_lists(list_list)
		IdController.fill_boards(board_list)
		return 'All OK'

	def get_interests(self):
		return Interest.objects.filter(ord_pos=0)

	def get_interest(self,key):
		return Interest.objects.get(key=key)

	def complete_interest(self, list_key):
		client = TrelloClient(
			api_key=self.conf['trello']['api_key'],
			token=self.conf['trello']['token'])
		item_list = Interest.objects.filter(list_key=list_key)
		count = len(item_list)
		num = random.randint(0, count - 1)
		interest = None
		for item in item_list:
			if item.ord_pos == 0:
				client.get_card(item.key).change_list(IdController.get_list_id_on_board('Закончено', 'Интересы'))
			if item.ord_pos == num:
				client.get_card(item.key).set_pos('top')
				interest = item
		return interest

	def fill_input_tasks(self):
		Task.objects.all().delete()
		print('Start fill input tasks')
		client = TrelloClient(
			api_key=self.conf['trello']['api_key'],
			token=self.conf['trello']['token'])
		print('connected')
		board_id = IdController.get_board_id('Прогресс')
		list_id = IdController.get_list_id_on_board('Входящие', 'Прогресс')
		board = client.get_board(board_id=board_id)
		lista = board.get_list(list_id)
		list_list = [lista]
		list_id = IdController.get_list_id_on_board('Распределить', 'Прогресс')
		listb = board.get_list(list_id)
		list_list.append(listb)

		for list in list_list:
			print("Load list : " + list.name)
			for card in list.list_cards():
				print('Load card ' + card.name)
				#Load special and description
				description = card.description
				special = ''
				special_start = '[special]('
				special_end = ')'
				if description.find(special_start) != -1:
					special = description[description.find(special_start) + len(special_start):description.find(special_end) - len(special_end) + 1]
					description = description[:description.find(special_start)]

				#Load duration
				name = card.name
				duration = 0
				duration_start = '['
				duration_end = ']'
				if name.find(duration_start) != -1:
					duration = name[name.find(duration_start) + len(duration_start):name.find(duration_end) - len(duration_end) + 1]
					name = name[:name.find(duration_start)]

				checkList =[]
				sub_task=''
				labels=[]
				card.fetch_checklists()

				#Load checklists
				if (len(card.checklists) > 0):
					for item in card.checklists[0].items:
						ch = ''
						if item['checked']:
							ch = ' +'
						checkList.append(item['name'] + ch)
						if (sub_task == '' and not item['checked']):
							sub_task = item['name']
					checkList.insert(0, card.checklists[0].name)
				# Если есть лейблы грузим их
				if (card.list_labels):
					labels = [x.name for x in card.list_labels]
				# Load image
				card.fetch_attachments(True)
				image = card.get_attachments()[0].url if len(card.get_attachments())>0 else ''
				task = Task(key=card.id,
				            name=name,
				            description=description,
				            duration=duration,
				            list_key=list.id,
				            checklist=";".join(checkList),
				            # due_date=card.due_date,
				            labels='NN',
				            special=special,
				            image=image
				            )
				task.save()
				print('card saved')
		return 'All OK'

	def get_input_tasks(self):
		list_id = IdController.get_list_id_on_board('Входящие', 'Прогресс')
		return Task.objects.filter(list_key=list_id)

	def get_distribute_tasks(self):
		list_id = IdController.get_list_id_on_board('Распределить', 'Прогресс')
		return Task.objects.filter(list_key=list_id)

	def update_input_task(self, task):
		client = TrelloClient(
			api_key=self.conf['trello']['api_key'],
			token=self.conf['trello']['token'])
		print('Connected')
		card = client.get_card(task.key)
		if task.image is not None:
			card.attach(url=task.image)
		if task.description is not None:
			card.set_description(task.description)
		#Если это интерес
		if task.list_key != IdController.get_list_id_on_board('Входящие', 'Прогресс'):
			print('Save interest')
			card.change_board(IdController.get_board_id('Интересы'), task.list_key)
			int = Interest(key = task.key,name = task.name, img = task.image,list_key = task.list_key,list_name = IdController.get_list_name(task.list_key),description = task.description,ord_pos = card.pos)
			int.save()
			task.delete()
			print('Complete')
		else:
			print('Save as task')
			ur_label = client.get_label(IdController.get_label_id_on_board('Срочные цели', 'Прогресс'), IdController.get_board_id('Прогресс'))
			nur_label = client.get_label(IdController.get_label_id_on_board('Не срочные цели', 'Прогресс'), IdController.get_board_id('Прогресс'))
			if task.labels == 'UI':
				card.add_label(ur_label)
				card.change_list(IdController.get_list_id_on_board('Распределить', 'Прогресс'))
				task.list_key = IdController.get_list_id_on_board('Распределить', 'Прогресс')
			elif task.labels == 'UN':
				card.add_label(ur_label)
				card.change_board(IdController.get_board_id('Неважное'), IdController.get_list_id_on_board( 'Срочное','Неважное'))
				task.list_key = IdController.get_list_id_on_board( 'Срочное','Неважное')
			elif task.labels == 'NI':
				card.add_label(nur_label)
				card.change_board(IdController.get_board_id('Цели'), IdController.get_list_id_on_board('Новые', 'Цели'))
				task.list_key = IdController.get_list_id_on_board('Новые', 'Цели')
			elif task.labels == 'NN':
				card.add_label(nur_label)
				card.change_board(IdController.get_board_id('Неважное'), IdController.get_list_id_on_board('Несрочное', 'Неважное'))
				task.list_key = IdController.get_list_id_on_board('Несрочное', 'Неважное')
			print('Task ' + task.name + ' set labels ' + task.labels)
			task.save()
		return 'All OK'

	def delete_task(self, key):
		client = TrelloClient(
			api_key=self.conf['trello']['api_key'],
			token=self.conf['trello']['token'])
		print('Connected')
		card = client.get_card(key)
		print('Delete task ' + card.name)
		card.delete()
		Task.objects.get(key=key).delete()

	def get_task_types(self):
		excludedTypes=['Входящие','Распределить','Пауза (В ожидании)','Выполненые','Сегодня']
		types=[]
		for type in IdController.get_board_lists_name('Прогресс'):
			if type not in excludedTypes:
				types.append(type)
		return ";".join(types)


	def create_hook(self):
		print('start creating trello hook')
		client = TrelloClient(
			api_key=self.conf['trello']['api_key'],
			token=self.conf['trello']['token'])
		client.create_hook('http://85.143.212.176/hook/trello','57e04a0fda82f763f66385a1')
		print('Done')


import json
import random
from trello import TrelloClient
from ..models import Interest
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
			print('board_added')
			for list in board.list_lists():
				card_list=[]
				l={}
				l['name'] = list.name
				l['key'] = list.id
				l['owner_key'] = board.id
				list_list.append(l)
				print('list_added')
				if add_cards:
					for card in list.list_cards():
						c={}
						c['name'] = card.name
						c['key'] = card.id
						c['owner_key'] = list.id
						card_list.append(c)
						print('card added')
					IdController.fill_cards(card_list)
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



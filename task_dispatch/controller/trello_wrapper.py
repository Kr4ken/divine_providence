import json
from trello import TrelloClient
from ..models import Interest
from django.conf import settings
from .trello.IdController import IdController

class TrelloWrapper:
	conf = json.load(open(settings.CONFIG_PATH, 'r', encoding="utf-8"))

	def fill_interests(self):
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
					interest = Interest(key=l.id, name=l.name, img=attach, list_key=card.name, description=card.desc,ord_pos=counter)
					interest.save()
					counter= counter + 1
				print(l.name + ' list ended')

	def fill_all(self):
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
		return Interest.objects.get(ord_pos=0)




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
				print('get cards for ' + l.name)
				for card in l.list_cards():
					print(card.name + ' performed')
					card.fetch_attachments(force=True)
					print(card.pos)
					interest = Interest(key=l.id, name=l.name, img=card.get_attachments()[0].url, list_key=card.name, description=card.desc,pos=card.pos)
					interest.save()
				print(l.name + ' list ended')







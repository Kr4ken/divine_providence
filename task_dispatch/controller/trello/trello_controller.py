import json
import random
from .interest import Interest

from datetime import datetime
from trello import TrelloClient


class TrelloController:
	def __init__(self, config="config.json"):
		conf = json.load(open(config, 'r', encoding="utf-8"))
		self.client = TrelloClient(
			api_key=conf['trello']['api_key'],
			token=conf['trello']['token'])
		self.interestIgnoredList = conf['app']['intersest']['ignoredList']

	def get_interest_list(self):
		res_list = []
		l_board = self.client.get_board('57e04a0fda82f763f66385a1')
		l_lists = l_board.all_lists()
		for l in l_lists:
			if l.name not in self.interestIgnoredList:
				card = l.list_cards()[0]
				card.fetch_attachments(force=True)
				interest = Interest(key=l.id, name=l.name, img=card.get_attachments()[0].url, value=card.name, description=card.desc)
				# interest = Interest(key=l.id, name=l.name, value="None")
				res_list.append(interest)
		return res_list

	def get_interest(self, list_key):
		l_board = self.client.get_board('57e04a0fda82f763f66385a1')
		l = l_board.get_list(list_key)
		card = l.list_cards()[0]
		card.fetch_attachments(force=True)
		return Interest(key=l.id, name=l.name, img=card.get_attachments()[0].url, value=card.name)

	def complete_interest(self, list_key):
		item_list = self.client.get_board('57e04a0fda82f763f66385a1').get_list(list_key)
		item_list.list_cards()[0].change_list('57e240893d95ffac689b8880')
		count = item_list.cardsCnt()
		num = random.randint(0, count - 1)
		item_list.list_cards()[num].set_pos('top')
		card = item_list.list_cards()[0]
		card.fetch_attachments(force=True)
		return Interest(key=item_list.id, name=item_list.name, img=card.get_attachments()[0].url, value=card.name, description=card.desc)

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.client.logout()

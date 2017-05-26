import json
import random
from .interest import Interest

from datetime import datetime
from trello import TrelloClient

class trello_controller:

	def __init__(self,config = "config.json"):
		conf = json.load(open(config, 'r'))
		self.client = TrelloClient(
			api_key=conf['trello']['api_key'],
			token=conf['trello']['token'])
		# Установка констант
		self.special_start = '[special]('
		self.special_end = ')'
		self.l_lists=[]

	def get_interest_list(self):
		res_list=[]
		l_board = self.client.get_board('57e04a0fda82f763f66385a1')
		self.l_lists = l_board.all_lists()
		count = 0
		for l in self.l_lists:
			card = l.list_cards()[0]
			card.fetch_attachments(force=True)
			interest = Interest(key=l.id,name=l.name,img=card.get_attachments()[0].url,value=card.name)
			res_list.append(interest)
			count += 1
		return res_list

	def get_interest(self,list_key):
		l_board = self.client.get_board('57e04a0fda82f763f66385a1')
		l = l_board.get_list(list_key)
		card = l.list_cards()[0]
		card.fetch_attachments(force=True)
		return  Interest(key=l.id,name=l.name,img=card.get_attachments()[0].url,value=card.name)

	def complete_interest(self,list_key):
		item_list = self.client.get_board('57e04a0fda82f763f66385a1').get_list(list_key)
		item_list.list_cards()[0].change_list('57e240893d95ffac689b8880')
		count = item_list.cardsCnt()
		num = random.randint(0, count - 1)
		item_list.list_cards()[num].set_pos('top')
		card = item_list.list_cards()[0]
		card.fetch_attachments(force=True)
		return  Interest(key=item_list.id,name=item_list.name,img=card.get_attachments()[0].url,value=card.name)

	def get_new_item_interst_list(self, list_index):
		response={}
		item_list = self.client.get_board('57e04a0fda82f763f66385a1').get_list(self.l_lists[list_index].id)
		item_list.list_cards()[0].change_list('57e240893d95ffac689b8880')
		count = item_list.cardsCnt()
		num = random.randint(0, count - 1)
		response['list_name'] = item_list.name
		response['item_name'] = item_list.list_cards()[num].name
		item_list.list_cards()[num].set_pos('top')
		return response

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.client.logout()

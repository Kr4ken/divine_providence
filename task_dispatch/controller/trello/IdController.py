from task_dispatch.models import IdObject


class IdController:
	@staticmethod
	def fill_boards(board_list):
		for board in board_list:
			id_object = IdObject(name=board['name'], key=board['key'], owner_key=None, type=IdObject.BOARD_TYPE)
			id_object.save()

	@staticmethod
	def fill_lists(list_list):
		for list in list_list:
			id_object = IdObject(name=list['name'], key=list['key'], owner_key=list['owner_key'], type=IdObject.LIST_TYPE)
			id_object.save()

	@staticmethod
	def fill_cards(card_list):
		for card in card_list:
			id_object = IdObject(name=card['name'], key=card['key'], owner_key=card['owner_key'], type=IdObject.CARD_TYPE)
			id_object.save()

	@staticmethod
	def get_board_id(board_name):
		try:
			id_object = IdObject.objects.get(name=board_name, type=IdObject.BOARD_TYPE)
		except IdObject.DoesNotExist:
			return False
		return id_object.key

	@staticmethod
	def get_list_id(list_name):
		try:
			id_object = IdObject.objects.get(name=list_name, type=IdObject.LIST_TYPE)
		except IdObject.DoesNotExist:
			return False
		return id_object.key



	@staticmethod
	def clear():
		IdObject.objects.all().delete()




from task_dispatch.models import IdObject


class IdController:
	@staticmethod
	def get_board_lists_name(board_name):
		names=[]
		for list in IdObject.objects.filter(owner_key=IdController.get_board_id(board_name),type=IdObject.LIST_TYPE):
			names.append(list.name)
		return names

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
	def fill_label(label):
		id_object = IdObject(name=label['name'],key=label['key'],owner_key=label['owner_key'],type=IdObject.LABEL_TYPE)
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
	def get_list_id_on_board(list_name, board_name):
		try:
			id_object = IdObject.objects.get(name=list_name, type=IdObject.LIST_TYPE, owner_key=IdController.get_board_id(board_name))
		except IdObject.DoesNotExist:
			return False
		return id_object.key

	@staticmethod
	def get_list_name(list_id):
		try:
			id_object = IdObject.objects.get(key=list_id, type=IdObject.LIST_TYPE)
		except IdObject.DoesNotExist:
			return False
		return id_object.name

	@staticmethod
	def get_label_id_on_board(label_name, board_name):
		try:
			id_object = IdObject.objects.get(name=label_name, type=IdObject.LABEL_TYPE, owner_key=IdController.get_board_id(board_name))
		except IdObject.DoesNotExist:
			return False
		return id_object.key

	@staticmethod
	def clear():
		IdObject.objects.all().delete()




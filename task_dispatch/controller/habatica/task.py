class Task(object):
	"""
	Class represented any task or habit
	"""
	@property
	def user_id(self):
		return self._user_id

	@property
	def text(self):
		return self._text

	@text.setter
	def text(self, value):
		self._text = value

	@property
	def alias(self):
		return self._alias

	@alias.setter
	def alias(self, value):
		self._alias = value

	@property
	def notes(self):
		return self._notes

	@notes.setter
	def notes(self, value):
		self._notes = value

	@property
	def tags(self):
		return self._tags

	@tags.setter
	def tags(self, value):
		self._tags = value

	@property
	def priority(self):
		return self._priority

	@priority.setter
	def priority(self, value):
		self._priority = value

	@property
	def attribute(self):
		return self._attribute

	@attribute.setter
	def attribute(self, value):
		self._attribute = value

	@property
	def type(self):
		return self._type

	@type.setter
	def type(self, value):
		self._type = value

	@property
	def comleted(self):
		return self._comleted

	@comleted.setter
	def comleted(self, value):
		self._comleted = value

	def __init__(self, client=None, task_id=None, task_name=''):
		self.client = client
		self.task_id = task_id
		self.name = task_name

	@classmethod
	def from_json(cls, client=None, json_obj=None):
		# print(json_obj)
		task = Task(client=client, task_id=json_obj['_id'])
		task._user_id = json_obj['userId']
		task._text = json_obj['text']
		task._alias = json_obj.get('alias','')
		task._notes = json_obj.get('notes','')
		task._tags = json_obj['tags']
		task._value = json_obj['value']
		task._priority = json_obj['priority']
		task._attribute = json_obj['attribute']
		task._comleted = json_obj['priority']
		task._type = json_obj['type']
		return task

	def save(self):
		pass

	# Fetch data about task
	def fetch(self):
		json_obj = self.client.fetch_json('/tasks/' + self.task_id)
		self._user_id = json_obj['data']['userId']
		self._text = json_obj['data']['text']
		self._alias = json_obj['data']['alias']
		self._notes = json_obj['data']['notes']
		self._tags = json_obj['data']['tags']
		self._value = json_obj['data']['value']
		self._priority = json_obj['data']['priority']
		self._attribute = json_obj['data']['attribute']
		self._comleted = json_obj['data']['priority']
		self._type = json_obj['data']['type']

	def __str__(self):
		return ''+ 'id:' +self.task_id+ ' text:' + self.text + ' notes:' + self.notes

	def add_tag(self,tag=None):
		#TODO:Realise this
		pass

	def add_checklist_item(self, item=None):
		#TODO:Realise this
		pass

	def change_checklist_item(self, item=None):
		#TODO:Realise this
		pass

	def delete_checklist_item(self, item=None):
		#TODO:Realise this
		pass

	def approve_users_task(self, user=None):
		#TODO:Realise this
		pass

	def assign_group_task(self, task=None):
		#TODO:Realise this
		pass


	def delete_tag(self, tag=None):
		#TODO:Realise this
		pass

	def delete(self):
		#TODO:Realise this
		pass

	def move_to(self):
		#TODO:Realise this
		pass

	def score_checklist_item(self, item=None):
		#TODO:Realise this
		pass

	def score(self):
		#TODO:Realise this
		pass






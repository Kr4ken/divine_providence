from .task import Task

class User(object):
	"""
	Class represented a habatica user
	This is the main class in hierarchy
	He contains almost all other classes
	"""

	@property
	def tasklist(self):
		try:
			if self._tasklist is None:
				self._tasklist = self.fetch_tasklist()
		except AttributeError:
			self._tasklist=None
		return self._tasklist

	def __init__(self, client = None):
		self.client = client
		self._tasklist= None

	@classmethod
	def from_json(cls,client = None,json_obj=None):
		user = User(client)
		#TODO:Сделать важные фетчи
		return user

	def fetch(self):
		self.client.fetch_json()

	def add_task(self, task):
		self.client.fetch_json(uri_path='/tasks/user',
		                       http_method='POST',post_args=task)

	def get_task_alias_id(self,alias_id):
		for task in self.tasklist:
			if alias_id == task.alias:
				return task
		return None

	def update_task(self,task):
		url = '/tasks/%s' % task['alias']
		self.client.fetch_json(uri_path= url,
							   http_method='PUT',post_args=task)

	def delete_task(self,task):
		url = '/tasks/%s' % task.task_id
		self.client.fetch_json(uri_path= url,
							   http_method='DELETE')
	# Костыль
	def delete_task_by_id(self,task):
		url = '/tasks/%s' % task
		self.client.fetch_json(uri_path= url,
							   http_method='DELETE')


	def sync_task(self,task):
		if(not self.get_task_alias_id(task.alias) is None):
			self.update_task(task)
		else:
			self.add_task(task)

	def fetch_tasklist(self):
		json_task_list = self.client.fetch_json(uri_path='/tasks/user')
		return [Task.from_json(self.client,task) for task in json_task_list['data']]

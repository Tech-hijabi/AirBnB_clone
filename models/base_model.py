#!/usr/bin/python3


from datetime import datetime
import models
import json
import uuid
class BaseModel:
	

	def __init__(self, *args, **kwargs):
		if kwargs:
			for key, value in kwargs.items():
				if key == 'created_at' or key == 'updated_at':

					value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
				if key != '__class__':
					setattr(self, key, value)
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = self.created_at
			models.storage.new(self)

	
	def __str__(self):
		return (
			f"[{self.__class__.__name__}] "
			f"({self.id})" 
			f"{self.__dict__}"
		)
	
	def save(self):
		self.updated_at = datetime.now()
		models.storage.save()


	def to_dict(self):
		dict = self.__dict__
		dict['__class__'] = self.__class__.__name__

		if 'created_at' in dict and isinstance(dict['created_at'], datetime):
			dict['created_at'] = dict['created_at'].isoformat()
		if 'updated_at' in dict and isinstance(dict['updated_at'], datetime):
			dict['updated_at'] = dict['updated_at'].isoformat()

		return dict

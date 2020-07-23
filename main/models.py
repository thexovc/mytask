from django.db import models
from django.conf import settings

# Todolist Model.

class Todolist(models.Model):
	task = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.item + ' | ' + str(self.completed)






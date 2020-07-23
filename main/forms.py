from django import forms
from .models import Todolist

class ListForm(forms.ModelForm):
	class Meta:
		model = Todolist
		fields = ["task", "completed"]


from django.shortcuts import render, redirect
from .models import Todolist
from .forms import ListForm
from django.contrib import messages

from main.models import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items = Todolist.objects.all
			messages.success(request, ('A Task Has Been Added To The List'))
			return render(request, 'home.html', {'all_items':all_items})

	else:
		all_items = Todolist.objects.all
		return render(request, 'home.html', {'all_items':all_items})

def delete(request, id):
	task = Todolist.objects.get(pk=id)
	task.delete()
	messages.success(request, ('A Task Has Been Deleted'))
	return redirect('main:home')

def check(request, id):
	task = Todolist.objects.get(pk=id)
	task.completed = True
	task.save()
	return redirect('main:home')

def uncheck(request, id):
	task = Todolist.objects.get(pk=id)
	task.completed = False
	task.save()
	return redirect('main:home')

def edit(request, id):
	if request.method == 'POST':
		task = Todolist.objects.get(pk=id)

		form = ListForm(request.POST or None, instance=task)

		if form.is_valid():
			form.save()
			messages.success(request, ('A Task Has Been Edited!'))
			return redirect('main:home')

	else:
		task = Todolist.objects.get(pk=id)
		return render(request, 'edit.html', {'task':task})




# User View


def start(request):
	return render(request, 'start.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

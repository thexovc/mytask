from django.contrib import admin
from .models import Todolist

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from main.models import *

# Register your models here.

admin.site.register(Todolist)


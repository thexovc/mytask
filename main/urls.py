# urls.py

from django.urls import path

from main.views import *

from django.contrib import admin






app_name = 'main'


urlpatterns = [
	path('home/', home, name='home'),
	path('delete/<id>', delete, name='delete'),
	path('check/<id>', check, name='check'),
	path('uncheck/<id>', uncheck, name='uncheck'),
	path('edit/<id>', edit, name='edit'),

	path('', start, name='start'),
    path('SignUp/', signup_view, name='signup_view'),
    

]


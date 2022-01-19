ToDo app with authentication in Django

-Installation:
pip install django
pip install psycopg2

-Usage:
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, path, include

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.db import models
from django import forms

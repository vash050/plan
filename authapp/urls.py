

from django.contrib import admin
from django.urls import path, include

import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('api/', authapp.CreateUserAPI.as_view()),
]

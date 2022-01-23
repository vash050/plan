from django.contrib import admin
from django.urls import path, include

import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('create-user/', authapp.CreateUserAPI.as_view()),
    path('read-parameters-body-user/<int:pk>/<str:date>/', authapp.ParametersBodyUser.as_view()),

]

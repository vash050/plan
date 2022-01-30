from django.contrib import admin
from django.urls import path, include

import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('api/v1/create-user/', authapp.CreateUserAPI.as_view()),
    path('api/v1/read-parameters-body-user/<int:pk>/<str:date>/', authapp.ParametersBodyUser.as_view()),

]

from django.contrib import admin
from django.urls import path, include

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    # path('plans-user/<int:pk>/', mainapp.PlanDaysApi.as_view()),
]

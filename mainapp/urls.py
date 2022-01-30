from django.contrib import admin
from django.urls import path, include

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('api/v1/plans-user/<str:plan_date>/', mainapp.PlanDaysApi.as_view()),
]

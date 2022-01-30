from django.contrib import admin
from django.urls import path, include

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('api/v1/plans-user/', mainapp.PlanWeekApi.as_view()),
    path('api/v1/create-plans-user/', mainapp.CreatePlanWeekApi.as_view()),
]

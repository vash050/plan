from django.contrib import admin

from mainapp.models import Muscles, Exercises, Plan, PlanUser

admin.site.register(Muscles)
admin.site.register(Exercises)
admin.site.register(Plan)
admin.site.register(PlanUser)
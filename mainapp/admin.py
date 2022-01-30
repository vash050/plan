from django.contrib import admin

from mainapp.models import Muscles, Exercises, ExerciseUser, PlanUser

admin.site.register(Muscles)
admin.site.register(Exercises)
admin.site.register(ExerciseUser)
admin.site.register(PlanUser)
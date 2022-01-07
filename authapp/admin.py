from django.contrib import admin

from authapp.models import UserSite, BodyParameters, UserBody, UserPlan

admin.site.register(UserSite)
admin.site.register(BodyParameters)
admin.site.register(UserBody)
admin.site.register(UserPlan)

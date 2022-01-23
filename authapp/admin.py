from django.contrib import admin

from authapp.models import UserSite, BodyParameters, UserBody, DataUserParameters

admin.site.register(UserSite)
admin.site.register(BodyParameters)
admin.site.register(UserBody)
admin.site.register(DataUserParameters)

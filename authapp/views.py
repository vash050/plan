from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from authapp.serializers import UserSiteSerializer


class CreateUserAPI(CreateAPIView):
    serializer_class = UserSiteSerializer

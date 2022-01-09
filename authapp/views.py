from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from authapp.models import DataUserParameters
from authapp.serializers import UserSiteSerializer, ParametersBodyUserSerializer


class CreateUserAPI(CreateAPIView):
    serializer_class = UserSiteSerializer


class ParametersBodyUser(RetrieveUpdateDestroyAPIView):
    serializer_class = ParametersBodyUserSerializer

    def get_queryset(self):
        queryset = DataUserParameters.objects.filter(user=self.request.user.id) or None
        return queryset


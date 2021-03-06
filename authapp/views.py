from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from authapp.models import DataUserParameters, UserBody
from authapp.serializers import UserSiteSerializer, UserBodySerializer


class CreateUserAPI(CreateAPIView):
    serializer_class = UserSiteSerializer


class ParametersBodyUser(RetrieveUpdateDestroyAPIView):
    serializer_class = UserBodySerializer

    def get_queryset(self):
        queryset = UserBody.objects.filter(id=self.kwargs['pk']).filter(date=self.kwargs['date'])
        print(self.kwargs['date'])
        print(queryset)
        return queryset

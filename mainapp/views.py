import datetime

from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from mainapp.models import PlanUser
from mainapp.serializers import PlanUserSerializer


class PlanDaysApi(ListAPIView):
    model = PlanUser
    serializer_class = PlanUserSerializer

    def get_queryset(self):
        plan = PlanUser.objects.filter(user=self.request.user).order_by('-plan_date')[:5]
        return plan



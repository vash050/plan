from rest_framework.generics import ListAPIView, CreateAPIView

from mainapp.models import PlanUser
from mainapp.serializers import PlanUserSerializer, CreatePlanUserSerializer


class PlanWeekApi(ListAPIView):
    model = PlanUser
    serializer_class = PlanUserSerializer

    def get_queryset(self):
        plan = PlanUser.objects.filter(user=self.request.user).order_by('-plan_date')[:5]
        return plan


class CreatePlanWeekApi(CreateAPIView):
    serializer_class = CreatePlanUserSerializer

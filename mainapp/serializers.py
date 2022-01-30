from rest_framework.serializers import ModelSerializer


from mainapp.models import PlanUser


class PlanUserSerializer(ModelSerializer):
    class Meta:
        model = PlanUser
        depth = 1
        fields = ('id', 'plan_date', 'plans', 'comment')

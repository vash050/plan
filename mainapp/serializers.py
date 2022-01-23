from rest_framework.serializers import ModelSerializer


from mainapp.models import Plan


class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        depth = 1
        fields = ('exercises', )


# class PlanUserSerializer(ModelSerializer):
#     all_plans = PlanSerializer(source="plan_set", many=True, read_only=True)
#
#     class Meta:
#         model = UserPlan
#         fields = ('user', 'all_plans', 'comment', 'date', 'plan')

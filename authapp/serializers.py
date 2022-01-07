from rest_framework.serializers import ModelSerializer

from authapp.models import UserSite


class UserSiteSerializer(ModelSerializer):
    class Meta:
        model = UserSite
        fields = ['id', 'first_name', 'last_name', 'date_born', 'height']

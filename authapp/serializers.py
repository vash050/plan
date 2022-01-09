from rest_framework.serializers import ModelSerializer

from authapp.models import UserSite, DataUserParameters


class UserSiteSerializer(ModelSerializer):
    class Meta:
        model = UserSite
        fields = ['id', 'first_name', 'last_name', 'date_born', 'height']

class UserSiteSerializer(ModelSerializer):
    class Meta:
        model = UserSite
        fields = ['id', 'first_name', 'last_name', 'date_born', 'height']


class ParametersBodyUserSerializer(ModelSerializer):
    all_parametrs = UserSerializer(source="dialog.members", many=True, read_only=True)

    class Meta:
        model = DataUserParameters
        fields = '__all__'

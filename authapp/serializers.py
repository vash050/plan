from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, ReadOnlyField

from authapp.models import UserSite, DataUserParameters, BodyParameters, UserBody


class UserSiteSerializer(ModelSerializer):
    class Meta:
        model = UserSite
        fields = ['id', 'first_name', 'last_name', 'date_born', 'height']


# class BodyParametersSerializer(ModelSerializer):
#     class Meta:
#         model = BodyParameters
#         fields = ('name', 'description')


class UserBodyParametersSerializer(ModelSerializer):

    class Meta:
        model = DataUserParameters
        depth = 1
        fields = ('parameter_body', 'data')


class UserBodySerializer(ModelSerializer):
    all_parameters = UserBodyParametersSerializer(source="datauserparameters_set", many=True, read_only=True)

    class Meta:
        model = UserBody
        fields = ('user', 'all_parameters', 'date', 'comment')

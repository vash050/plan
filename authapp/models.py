from django.db import models
from django.contrib.auth.models import AbstractUser

from mainapp.models import Plan


class UserSite(AbstractUser):
    date_born = models.DateField(verbose_name="день рождения", null=True)
    height = models.IntegerField(verbose_name='рост')


class BodyParameters(models.Model):
    name = models.CharField(max_length=240, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')


class UserBody(models.Model):
    user = models.ForeignKey(to=UserSite, on_delete=models.CASCADE)
    body_parameter = models.ForeignKey(to=BodyParameters, on_delete=models.CASCADE)
    date = models.DateField()
    data_parameter = models.IntegerField()
    comment = models.TextField(verbose_name='комментарии')


class UserPlan(models.Model):
    user = models.ForeignKey(to=UserSite, on_delete=models.CASCADE)
    plan = models.ForeignKey(to=Plan, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='комментарии')

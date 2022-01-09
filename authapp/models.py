from django.db import models
from django.contrib.auth.models import AbstractUser

from mainapp.models import Plan


class UserSite(AbstractUser):
    date_born = models.DateField(verbose_name="день рождения", null=True)
    height = models.IntegerField(verbose_name='рост', null=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class BodyParameters(models.Model):
    name = models.CharField(max_length=240, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', blank=True)

    class Meta:
        verbose_name = 'параметр тела'
        verbose_name_plural = 'параметры тела'

    def __str__(self):
        return self.name


class UserBody(models.Model):
    user = models.ForeignKey(to=UserSite, on_delete=models.CASCADE)
    body_parameter = models.ManyToManyField(to=BodyParameters, through='DataUserParameters')
    date = models.DateField()
    comment = models.TextField(verbose_name='комментарии', blank=True)

    class Meta:
        verbose_name = 'параметр тела пользователя'
        verbose_name_plural = 'параметры тела пользователя'

    def __str__(self):
        return f'параметры тела {self.user.username}'


class UserPlan(models.Model):
    user = models.ForeignKey(to=UserSite, on_delete=models.CASCADE)
    plan = models.ForeignKey(to=Plan, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='комментарии', blank=True)

    class Meta:
        verbose_name = 'план пользователь'
        verbose_name_plural = 'планы пользователя'


class DataUserParameters(models.Model):
    user = models.ForeignKey(UserBody, on_delete=models.CASCADE)
    parameter_body = models.ForeignKey(BodyParameters, on_delete=models.CASCADE)
    data = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'данные параметра тела пользователя'
        verbose_name_plural = 'данные параметра тела пользователя'

    def __str__(self):
        return f'данные параметра {self.parameter_body.name} тела пользователя {self.user.user.username}'

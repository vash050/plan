from django.db import models

from authapp.models import UserSite


class Muscles(models.Model):
    name = models.CharField(max_length=120, verbose_name='группа мышц')
    description = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name = 'группа мышц'
        verbose_name_plural = 'группы мышц'

    def __str__(self):
        return self.name


class Exercises(models.Model):
    name = models.CharField(max_length=120, verbose_name='название')
    description = models.TextField(verbose_name='описание', blank=True)
    movie = models.URLField(blank=True)
    muscle = models.ManyToManyField(to=Muscles)

    class Meta:
        verbose_name = 'упражнение'
        verbose_name_plural = 'упражнения'

    def __str__(self):
        return self.name


class Plan(models.Model):
    exercises = models.ManyToManyField(to=Exercises)
    counter = models.IntegerField(verbose_name='подходы')
    replay = models.IntegerField(verbose_name='повторения')
    weight = models.IntegerField(verbose_name='вес', null=True)
    comment = models.TextField(verbose_name='комментарии', blank=True)

    class Meta:
        verbose_name = 'запланированое упражнение'
        verbose_name_plural = 'запланированные упражнения'


class PlanUser(models.Model):
    user = models.ForeignKey(to=UserSite, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    plans = models.ManyToManyField(Plan)
    comment = models.TextField(verbose_name='комментарии', blank=True)

    def __str__(self):
        return f'План на {self.date}'

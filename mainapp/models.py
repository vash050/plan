from django.db import models


class Muscles(models.Model):
    name = models.CharField(max_length=120, verbose_name='группа мышц')
    description = models.TextField(verbose_name='описание')


class Exercises(models.Model):
    name = models.CharField(max_length=120, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    movie = models.URLField()
    muscle = models.ForeignKey(to=Muscles, on_delete=models.CASCADE)


class Plan(models.Model):
    date = models.DateField()
    exercises = models.ForeignKey(to=Exercises, on_delete=models.CASCADE)
    counter = models.IntegerField(verbose_name='подходы')
    replay = models.IntegerField(verbose_name='повторения')
    weight = models.IntegerField(verbose_name='вес')
    comment = models.TextField(verbose_name='комментарии')

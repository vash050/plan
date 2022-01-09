from django.db import models


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
    date = models.DateField()
    exercises = models.ForeignKey(to=Exercises, on_delete=models.CASCADE)
    counter = models.IntegerField(verbose_name='подходы')
    replay = models.IntegerField(verbose_name='повторения')
    weight = models.IntegerField(verbose_name='вес', null=True)
    comment = models.TextField(verbose_name='комментарии', blank=True)

    class Meta:
        verbose_name = 'запланированое упражнение'
        verbose_name_plural = 'запланированные упражнения'

    def __str__(self):
        return self.exercises.name

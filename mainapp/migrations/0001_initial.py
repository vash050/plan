# Generated by Django 4.0.1 on 2022-01-30 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='название')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('movie', models.URLField(blank=True)),
            ],
            options={
                'verbose_name': 'упражнение',
                'verbose_name_plural': 'упражнения',
            },
        ),
        migrations.CreateModel(
            name='ExerciseUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(verbose_name='подходы')),
                ('replay', models.IntegerField(verbose_name='повторения')),
                ('weight', models.IntegerField(null=True, verbose_name='вес')),
                ('comment', models.TextField(blank=True, verbose_name='комментарии')),
                ('exercises', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.exercises')),
            ],
            options={
                'verbose_name': 'запланированое упражнение',
                'verbose_name_plural': 'запланированные упражнения',
            },
        ),
        migrations.CreateModel(
            name='Muscles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='группа мышц')),
                ('description', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'группа мышц',
                'verbose_name_plural': 'группы мышц',
            },
        ),
        migrations.CreateModel(
            name='PlanUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('comment', models.TextField(blank=True, verbose_name='комментарии')),
                ('plans', models.ManyToManyField(to='mainapp.ExerciseUser')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'план пользователя',
                'verbose_name_plural': 'планы пользователя',
            },
        ),
        migrations.AddField(
            model_name='exercises',
            name='muscle',
            field=models.ManyToManyField(to='mainapp.Muscles'),
        ),
    ]

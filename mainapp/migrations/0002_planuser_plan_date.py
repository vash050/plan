# Generated by Django 4.0.1 on 2022-01-30 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planuser',
            name='plan_date',
            field=models.DateField(default='2022-02-01'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.8 on 2022-10-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='day',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='mesocycle',
            name='mesocycle',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='week',
            name='week',
            field=models.IntegerField(default=1),
        ),
    ]

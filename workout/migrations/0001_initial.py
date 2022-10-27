# Generated by Django 4.0.8 on 2022-10-27 16:43

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
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.CharField(max_length=200)),
                ('focus', models.CharField(max_length=200)),
                ('url', models.URLField(max_length=300)),
                ('tenRepMax', models.IntegerField()),
                ('type', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mesocycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setCount', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('repGoal', models.IntegerField()),
                ('repResult', models.IntegerField()),
                ('sorenessRating', models.IntegerField()),
                ('pumpRating', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout.day')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('mesocycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout.mesocycle')),
            ],
        ),
        migrations.AddField(
            model_name='day',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout.week'),
        ),
    ]
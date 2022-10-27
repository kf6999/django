from django.db import models
from django.urls import reverse


class Mesocycle(models.Model):
    mesocycle = models.CharField(default=1, max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mesocycle


class Week(models.Model):
    week = models.CharField(default=1, max_length=200)
    mesocycle = models.ForeignKey(Mesocycle, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.week


class Day(models.Model):
    day = models.CharField(default=1,max_length=200)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.day


class Exercise(models.Model):
    exercise = models.CharField(max_length=200)
    focus = models.CharField(max_length=200)
    url = models.URLField(max_length=300)
    tenRepMax = models.IntegerField()
    type = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.exercise


class Workout(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    setCount = models.IntegerField()
    weight = models.IntegerField()
    repGoal = models.IntegerField()
    repResult = models.IntegerField()
    sorenessRating = models.IntegerField()
    pumpRating = models.IntegerField()
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    creator = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.exercise.exercise

    def get_absolute_url(self):
        return reverse("workout_detail", kwargs={"pk": self.pk})

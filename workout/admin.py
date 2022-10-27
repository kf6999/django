from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Mesocycle)
admin.site.register(Week)
admin.site.register(Day)
admin.site.register(Exercise)
admin.site.register(Workout)


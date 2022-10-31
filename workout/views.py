from django.views.generic import ListView
from .models import *


class MesocycleListView(ListView):
    model = Mesocycle
    template_name = "mesocycle.html"


class WeekListView(ListView):
    model = Week
    weeks = Week.objects.select_related().all()
    template_name = "week.html"


class DayListView(ListView):
    model = Day
    template_name = "day.html"

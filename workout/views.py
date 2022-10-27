from django.views.generic import ListView
from .models import *


class MesocycleListView(ListView):
    model = Mesocycle
    template_name = "mesocycle.html"
from django.urls import path
from .views import MesocycleListView

urlpatterns = [
    path("", MesocycleListView.as_view(), name="mesocycle"),
]

from django.urls import path
from .views import MesocycleListView, WeekListView

urlpatterns = [
    path("mesocycle/<int:pk>", WeekListView.as_view(), name="week"),
    path("", MesocycleListView.as_view(), name="mesocycle"),
]

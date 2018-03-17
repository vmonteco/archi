from django.urls import path
from django.views.generic import ListView
from .models import Picture

urlpatterns = [
    path('', ListView.as_view(model=Picture)),
]

from django.urls import path
from . import views

app_name = "exhibition"

urlpatterns = [
  path('', views.exhibition_place, name="exhibition_places")
]
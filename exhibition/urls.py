from django.urls import path
from . import views

urlpatterns = [
  path('exhibitions/', views.exhibition_place, name="exhibition_places")
]
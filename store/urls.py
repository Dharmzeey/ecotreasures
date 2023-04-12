from django.urls import path
from . import views

app_name = "item"

urlpatterns = [
  path('details/<int:pk>/', views.item_details, name="item_details"),
]
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('<str:category>/', views.category_filter, name="home"),
]
from django.urls import path
from genba import views

urlpatterns = [
    path('', views.home, name="home"),
]

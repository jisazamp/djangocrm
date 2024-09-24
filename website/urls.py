from django.urls import path
from . import views

urlpatterns = [
    path("holamundo/", views.home_page, name="holamundo"),
]

from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("addpoll", views.addpoll, name="addpoll")
]
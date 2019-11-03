from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("<str:name>/", greet_someone, name="index"),
]

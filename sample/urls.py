from django.urls import path
from . import views

urlpatterns = [
    path("api/sample", views.sample),
]

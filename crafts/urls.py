from . import views
from django.urls import path

urlpatterns = [
    path("", views.Categories.as_view(), name="home"),
]

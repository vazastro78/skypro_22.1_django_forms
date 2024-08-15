from django.urls import path
from dealer.views import index

urlpatterns = [
    path("", index),
]

from django.urls import path
from .views import HomeView

urlpatterns=[
    path('',HomeView,name="bosh_sahifa"),
]


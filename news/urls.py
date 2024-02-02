from django.urls import path
from .views import HomeView,DetailNew,SportView

urlpatterns=[
    path('',HomeView,name="bosh_sahifa"),
    path('sport/',SportView,name="sportn"),
    path('detail/<slug:slug>/',DetailNew,name="detailn"),
]


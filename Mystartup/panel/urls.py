from django.contrib import admin
from django.urls import path,include
from . import views as panelviews

urlpatterns = [
    path('',panelviews.dashboard,name="dashboard"),
    path('profile/',panelviews.Profile_page,name="Profile"),
    path('toggle/',panelviews.toggle,name="toggle"),
    path('connect/',panelviews.connect,name="connect"),
    path('accept/',panelviews.accept,name="accept"),
    path('reject/',panelviews.reject,name="reject"),
]
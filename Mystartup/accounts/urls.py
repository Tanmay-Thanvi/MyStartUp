from django.contrib import admin
from django.urls import path,include

from . import views as accountsviews
from panel.views import home as panelhome
urlpatterns = [
    path('',panelhome,name="home"),
    path('login/',accountsviews.login,name="login"),
    path('register/',accountsviews.register,name="register"),
    path('logout/',accountsviews.logout,name="logout"),
    path('complete/',accountsviews.complete_profile,name="complete"),
    path('edit/',accountsviews.edit_profile,name="edit"),
]
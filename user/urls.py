from django.contrib import admin
from django.urls import path
from user import views
urlpatterns = [
    path("",views.user, name="user"),
    #path('login', views.login, name='login')
]

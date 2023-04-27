from django.contrib import admin
from django.urls import path,re_path,include
from .views import *
urlpatterns = [
    path('login/',login_page,name="login"),
    # path('register/',register,name="register"),
    path('logout/',logout_user,name="logout"),
]

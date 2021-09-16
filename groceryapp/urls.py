from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('dash', views.dash),
    path('breakfast', views.breakfast),
    path('lunch', views.lunch),
    path('dinner', views.dinner),
    path('user', views.user),
    path('addbgenre', views.addbgenre),
    path('createbgenre', views.createbgenre)
]
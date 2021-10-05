from django.urls import path

from. import views


urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('login', views.login),
    path('logout', views.logout),
    path('dash', views.dash),
    path('bld', views.bld),
    # path('lunch', views.lunch),
    # path('dinner', views.dinner),
    path('user', views.user),
    path('addgenre', views.addgenre),
    path('creategenre', views.creategenre),
    path('createing', views.createing),
    path('choice', views.TodChoice),
    path('delete/<int:theid>', views.delete)
]
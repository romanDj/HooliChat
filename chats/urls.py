from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('sigin/', views.sigin, name='sigin'),
    path('mychats/', views.mychats, name='mychats'),
    path('mychats/<int:interl_id>/', views.mychats, name='mychats'),
    path('profil/', views.profil, name='profil'),
    path('logout/', views.logoutDef, name='logout'),
    path('users/', views.users, name='users'),
    path('registration/', views.RegisterFormView.as_view(), name='registration'),
    path('lol/', views.lol, name='lol'),
]

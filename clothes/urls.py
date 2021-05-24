from django.urls import path
from . import views

urlpatterns = [
#path('', views.index, name='index'),
 path('', views.my_view, name='home'),
 path('female/', views.female, name='female'),
 path('male/', views.male, name='male'),
 path('select/', views.select, name='select'),
 path('femaleb/', views.femaleb, name='femaleb'),
 path('maleb/', views.maleb, name='maleb'),
]

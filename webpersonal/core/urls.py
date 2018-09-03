from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('store/', views.store, name="store"),
    path('mision/', views.mision, name="mision"),
    path('sample', views.sample, name="sample")
]

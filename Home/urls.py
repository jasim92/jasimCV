from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('my_cv/', views.about, name='My CV'),
    path('contact/', views.contact, name='Contact Us'),
]
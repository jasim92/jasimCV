from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.projects, name='My Projects'),
    path('/<str:slug>', views.content, name='Project Contents'),

]
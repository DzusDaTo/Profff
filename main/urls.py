from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.index, name='home'),
    path('index_sch/', views.index_sch, name='index_sch'),
    path('event/', views.event, name='event'),
    path('application/', views.application, name='application')
]
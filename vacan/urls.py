from django.urls import path, include
from .import views


urlpatterns = [
    path('vacan', views.news_out1, name='vacan'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail2'),

    ]
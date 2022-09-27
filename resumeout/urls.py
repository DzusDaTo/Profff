from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.news_out, name='resumeout'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail1'),

    ]
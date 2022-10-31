from django.urls import path

from . import views

urlpatterns = [
    path('information/video/', views.VideoViewSet.as_view(), name='video'),
]

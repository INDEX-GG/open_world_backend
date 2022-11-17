from django.urls import path

from . import views

urlpatterns = [
    path('information/video/', views.VideoAPIView.as_view()),
    path('information/games/', views.GamesAPIView.as_view()),
    path('information/games/<int:pk>/', views.GamesItemAPIView.as_view()),
    path('information/recommendations/', views.RecommendationsAPIView.as_view()),
    path('contacts/', views.ContactsAPIView.as_view()),
    path('about/', views.AboutAPIView.as_view()),
]

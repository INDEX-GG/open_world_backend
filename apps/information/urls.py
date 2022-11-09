from django.urls import path

from . import views

urlpatterns = [
    path('information/video/', views.VideoViewSet.as_view()),
    path('information/recommendations/', views.RecommendationsViewSet.as_view()),
    path('contacts/', views.ContactsViewSet.as_view()),
    path('about/', views.AboutViewSet.as_view()),
]

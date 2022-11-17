from django.urls import path

from . import views

urlpatterns = [
    path('news/', views.NewsAPIView.as_view()),
    path('news/<int:pk>/', views.NewsItemAPIView.as_view()),
]

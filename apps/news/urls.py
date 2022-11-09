from django.urls import path

from . import views

urlpatterns = [
    path('news/', views.NewsViewSet.as_view()),
    path('news/<int:pk>/', views.NewsItemViewSet.as_view()),
]

from django.urls import path

from apps.services import views

urlpatterns = [
    path('services/offline/', views.ServicesOfflineAPIView.as_view()),
    path('services/video/', views.ServicesVideoAPIView.as_view()),
]

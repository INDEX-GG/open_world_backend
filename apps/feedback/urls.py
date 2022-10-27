from django.urls import path

from apps.feedback import views

urlpatterns = [
    path('feedback/', views.FeedbackAPIView.as_view(), name='feedback'),
]

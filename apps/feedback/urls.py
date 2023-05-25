from django.urls import path

from apps.feedback import views

urlpatterns = [
    path('feedback/form/', views.FeedbackAPIView.as_view()),
    path('feedback/questions/', views.QuestionsAPIView.as_view()),
    path('feedback/questions/<int:pk>/', views.QuestionsItemAPIView.as_view()),
    path('feedback/', views.FeedbackMessageAPIView.as_view()),
]

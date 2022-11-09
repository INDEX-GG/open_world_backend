from django.urls import path

from apps.feedback import views

urlpatterns = [
    path('feedback/form/', views.FeedbackAPIView.as_view()),
    path('feedback/questions/', views.QuestionsViewSet.as_view()),
    path('feedback/questions/<int:pk>/', views.QuestionsItemViewSet.as_view()),
]

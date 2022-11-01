from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('auth/registration/send-code/', views.SendCodeView.as_view()),
    path('auth/registration/confirmation-code/', views.ConfirmationCodeAPIView.as_view()),
    path('auth/registration/', views.UserRegistrationView.as_view()),
    path('auth/login/', views.LoginAPIView.as_view()),
    path('auth/logout/', views.LogoutAPIView.as_view()),
    path('auth/reset-password/send-code/', views.ResetSendCodeView.as_view()),
    path('auth/reset-password/confirmation-code/', views.ResetConfirmationCodeAPIView.as_view()),
    path('auth/reset-password/', views.ResetPasswordAPIView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
]

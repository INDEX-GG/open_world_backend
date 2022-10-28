from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('auth/registration/send-code/', views.SendCodeView.as_view(), name='registration_send_code'),
    path('auth/registration/confirmation-code/', views.ConfirmationCodeAPIView.as_view(),
         name='registration_confirmation_code'),
    path('auth/registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('auth/login/', views.LoginAPIView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

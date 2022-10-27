from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('auth/registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('auth/registration/email-for-verifications/', views.EmailForVerificationView.as_view(), name='registration'),
    path('auth/registration/email-verify/', views.VerifyCodeAPIView.as_view(), name='registration'),
    path('auth/login/', views.LoginAPIView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

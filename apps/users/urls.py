from django.urls import path
from . import views


urlpatterns = [
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    # path('email-verify/', views.VerifyEmail.as_view(), name='email_verify'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('auth/admin/login/', views.LoginAdminAPIView.as_view()),
    path('auth/admin/logout/', views.LogoutAdminAPIView.as_view()),
]

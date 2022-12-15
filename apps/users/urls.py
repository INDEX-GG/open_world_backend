from django.urls import path

from apps.users import views

urlpatterns = [
    path('user/', views.UserDetailsAPIView.as_view()),
    path('user/delete/', views.UserDeleteAPIView.as_view()),
    path('children/', views.ChildrenAPIView.as_view()),
    path('children/<int:pk>/', views.ChildrenItemAPIView.as_view()),
]

from django.urls import path

from . import views

urlpatterns = [
    path('user/', views.UserDetailsView.as_view()),
    path('children/', views.ChildrenViewSet.as_view()),
    path('children/<int:pk>/', views.ChildrenItemViewSet.as_view()),
]

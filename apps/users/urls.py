from django.urls import path

from . import views

urlpatterns = [
    path('user/', views.UserDetailsView.as_view(), name='user'),
    path('children/', views.ChildrenViewSet.as_view(), name='children'),
    path('children/<int:pk>/', views.ChildrenItemViewSet.as_view(), name='user'),
]

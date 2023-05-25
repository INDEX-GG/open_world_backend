from django.urls import path
from apps.catalog.views import *


urlpatterns = [
    path('catalog/', SectionsAPIView.as_view(), name='catalog'),
    path('catalog/contacts/', TableContactsAPIView.as_view(), name='contacts'),
    path('catalog/worktime/', TableWorktimeAPIView.as_view(), name='worktime'),
    path('catalog/page/<path:path_value>/', ContentElementsAPIView.as_view(), name='content-elements'),
    path('search/', SearchAPIView.as_view(), name='search'),
]


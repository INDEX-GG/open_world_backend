from django.urls import path
from apps.catalog.views import *


urlpatterns = [
    path('catalog/', SectionsAPIView.as_view(), name='catalog'),
    path('catalog/<path:path_value>/', SectionsAPIView.as_view(), name='catalog-path'),
    path('table/contacts/', TableContactsAPIView.as_view(), name='contacts'),
    path('table/worktime/', TableWorktimeAPIView.as_view(), name='worktime'),
    path('page/<path:path_value>/', CatalogElementsAPIView.as_view(), name='content-elements'),
    path('search/', SearchAPIView.as_view(), name='search'),
    path('task/', GosTaskAPIView.as_view(), name='gos-task'),
]


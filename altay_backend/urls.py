from django.contrib import admin
from django.urls import path, include

from apps.base.yasg import urlpatterns as doc_urls
from apps.base.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('apps.users.urls')),
    path('api/v1/', include('apps.authentication.urls')),
    path('api/v1/', include('apps.feedback.urls')),
]

urlpatterns += doc_urls

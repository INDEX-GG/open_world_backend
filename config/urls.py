from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from apps.base.yasg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.users.urls')),
    path('api/v1/', include('apps.authentication.urls')),
    path('api/v1/', include('apps.feedback.urls')),
    path('api/v1/', include('apps.information.urls')),
    path('api/v1/', include('apps.services.urls')),
    path('api/v1/', include('apps.news.urls')),
    path('api/v1/', include('apps.catalog.urls')),
]

urlpatterns += doc_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

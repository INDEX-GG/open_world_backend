from django.contrib import admin
from django.urls import path
from altay_backend.yasg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += doc_urls

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from apps.base.yasg import urlpatterns as doc_urls
from apps.base.routers import router

# from dj_rest_auth.registration.views import VerifyEmailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('apps.users.urls')),

    # path('api/v1/auth/', include('dj_rest_auth.urls')),
    # path('api/v1/auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('api/v1/auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
]

urlpatterns += doc_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


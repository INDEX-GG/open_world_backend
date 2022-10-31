from apps.news.views import *
from apps.information.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'information/games', GamesViewSet)

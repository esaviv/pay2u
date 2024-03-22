from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .views import SubcriptionViewSet, CashbackViewSet


router = DefaultRouter()
router.register('subscriptions', SubcriptionViewSet)
router.register('cashback', CashbackViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, InsuranceViewSet, PolicyHolderViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('insurance', InsuranceViewSet, basename='insurance')
router.register('policy', PolicyHolderViewSet, basename='policy')

urlpatterns = router.urls

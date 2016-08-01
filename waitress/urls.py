from django.conf import settings
from django.conf.urls.static import static

from app.viewsets import MealSessionViewSet, UserViewSet, ReportViewSet
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'meal-sessions', MealSessionViewSet)
router.register(r'users', UserViewSet)
router.register(r'reports', ReportViewSet)

urlpatterns = [
    url(r'^', include(router.urls, namespace='api')),
    url(r'^docs/?', include('rest_framework_swagger.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

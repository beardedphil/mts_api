from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from sources.urls import router as sources_router
from articles.urls import router as articles_router

router = routers.DefaultRouter()
router.registry.extend(sources_router.registry)
router.registry.extend(articles_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('sources', views.SourceView)

urlpatterns = [
    path('', include(router.urls)),
]

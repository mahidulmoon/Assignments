from django.urls import path,include
from rest_framework import routers
from .views import MovieViewSet


router = routers.DefaultRouter()
router.register('movielist',MovieViewSet)


urlpatterns = [
    path('',include(router.urls)),
]
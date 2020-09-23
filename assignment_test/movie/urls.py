from django.urls import path,include
from rest_framework import routers
from .views import MovieViewSet,RatingViewSet


router = routers.DefaultRouter()
router.register('movielist',MovieViewSet)
router.register('ratinglist',RatingViewSet)


urlpatterns = [
    path('',include(router.urls)),
]
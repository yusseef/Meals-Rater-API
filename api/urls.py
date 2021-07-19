from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import MealViewSet, RatingViewSet
router = routers.DefaultRouter()
router.register('meals', MealViewSet, basename='meals')
router.register('ratings', RatingViewSet, basename='ratings')
urlpatterns = [
   path('', include(router.urls))
]

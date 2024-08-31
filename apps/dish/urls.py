from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('dish', DishViewSet, basename='dish')
router.register('recipie', RecipieViewSet, basename='recipie')


urlpatterns = [
    path('', include(router.urls)),
    
]

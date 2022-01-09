from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import TagViewSet, ServingSizeViewSet, IngredientViewSet, RecepieViewSet, RecepieLineViewSet


router = routers.DefaultRouter()
router.register('tag', TagViewSet)
router.register('servingsize', ServingSizeViewSet)
router.register('ingredient', IngredientViewSet)
router.register('recepie', RecepieViewSet)
router.register('recepie_line', RecepieLineViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
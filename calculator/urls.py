from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CalculatorView

router = DefaultRouter()
router.register(r'calculator',CalculatorView,'calculator')

urlpatterns = [
    path('api/',include(router.urls))
]

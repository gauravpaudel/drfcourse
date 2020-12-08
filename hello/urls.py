from django.urls import path
from .views import HelloApi, hello_drf

urlpatterns = [
    path('demo1/',HelloApi.as_view(),name='demo1'),
    path('demo2/',hello_drf,name='demo2')
]
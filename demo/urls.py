from django.contrib import admin
from django.urls import path,include
from hello.views import HelloApi,hello_drf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',include('hello.urls')),
    path('cal/',include('calculator.urls')),
    path('em/',include('employee.urls'))
]

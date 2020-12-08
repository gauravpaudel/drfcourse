from django.urls import path
from .views import EmployeeRUDView, EmployeeView

urlpatterns =[
    
    path('api/employees/<int:pk>/',EmployeeRUDView.as_view(),name='employee_rudview'),
    path('api/employees/',EmployeeView.as_view(),name='employee_view')

]
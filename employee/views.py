from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self,pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            context = {
                'message': 'Not Found'
            }
            return Response(context , status =status.HTTP_404_NOT_FOUND)
        return employee

    def get(self,request,pk):
        employee = self.get_queryset(pk)
        serializer = EmployeeSerializer(employee)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #update
    def put(self,request,pk):
        employee = self.get_queryset(pk)
        serializer = EmployeeSerializer(employee, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete
    def delete(self,request,pk):
        employee = self.get_queryset(pk)
        employee.delete()
        content = {
            'message':'Data was deletetd'
        }
        
        return Response(content, status=status.HTTP_204_NO_CONTENT)

class EmployeeView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        employees = Employee.objects.all()

        return employees

    def get(self,request):
        employees = self.get_queryset()

        serializer = self.serializer_class(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            
        return Respones(serializer.data,status=status.HTTP_400_BAD_REQUEST)
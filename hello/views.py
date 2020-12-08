from django.shortcuts import render

#rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.decorators import api_view

class HelloApi(APIView):
    def get(self,request):
        data = {'message':'Hello Django fellows'}
        return Response(data)

@api_view(['GET'])
def hello_drf(request):
    data = {'message':'Hello Django REst'}
    return Response(data)
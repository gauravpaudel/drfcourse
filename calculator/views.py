from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Numeric
from .serializers import NumericSerializer

class CalculatorView(viewsets.ModelViewSet):
    queryset = Numeric.objects.all()
    serializer_class = NumericSerializer

    @action(methods=['post'],detail=False)
    def add(self,request):
        print(request.data)
        serializer = NumericSerializer(data = request.data)
        print(serializer)

        if serializer.is_valid():
            numeric = serializer.validated_data
            numeric['result'] = numeric['numa'] + numeric['numb']

            return Response(numeric)
        else:
            print(serializer.errors)
        
        return Response({'status':'error','message':'invalid request'})


    @action(methods=['post'],detail=False)
    def substract(self,request):
        serializer = NumericSerializer(data=request.data)
        if serializer.is_valid():
            numeric = serializer.validated_data
            numeric['result'] = numeric['numa'] - numeric['numb']

            return Response(numeric)
        else:
            print(serilaizer.errors)
        
        return Response({'status':'error','message':'invalid request'})
    
    @action(methods=['post'],detail=False)
    def multiply(self,request):
        serializer = NumericSerializer(data=request.data)
        if serializer.is_valid():
            numeric = serializer.validated_data
            numeric['result'] = numeric['numa'] * numeric['numb']

            return Response(numeric)
        else:
            print(serializer.errors)

        return Response({'status':'errors','mesasge':'invalid request'})
    
    @action(methods = ['post'],detail = False)
    def divide(self,request):
        serializer = NumericSerializer(data=request.data)
        if serializer.is_valid():
            numeric = serializer.validated_data
            numeric['result'] = numeric['numa'] / numeric['numb']
            return Response(numeric)
        else:
            print(serializer.errors)

        return Response({'status':'errors','message':'invalid request'})
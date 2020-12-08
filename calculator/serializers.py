from rest_framework import serializers
from .models import Numeric

class NumericSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numeric
        fields = ['numa','numb','result']
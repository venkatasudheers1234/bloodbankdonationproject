from rest_framework import serializers
from . models import donor
from . models import blood
from . models import hospital
from . models import bloodBank
from . models import Employee
from . models import orders


class donorSerializer(serializers.ModelSerializer):

    class Meta:
        model = donor
        fields = '__all__'



class bloodSerializer(serializers.ModelSerializer):

    class Meta:
        model = blood
        fields = '__all__'

class hospitalSerializer(serializers.ModelSerializer):

    class Meta:
        model = hospital
        fields = '__all__'

class bloodBankSerializer(serializers.ModelSerializer):

    class Meta:
        model = bloodBank
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

class ordersSerializer(serializers.ModelSerializer):

    class Meta:
        model = orders
        fields = '__all__'






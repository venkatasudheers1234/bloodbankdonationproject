from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import donor
from . models import blood
from . models import hospital
from . models import bloodBank
from . models import Employee
from . models import orders


from . serializers import donorSerializer
from . serializers import bloodSerializer
from . serializers import hospitalSerializer
from . serializers import bloodBankSerializer
from . serializers import EmployeeSerializer
from . serializers import ordersSerializer





class donorList(APIView):

    def get(self,request):
        donor1 = donor.objects.all()
        serializer=donorSerializer(donor1,many=True)
        return Response(serializer.data)

    def post(self):
        pass


class bloodList(APIView):

    def get(self,request):
        blood1=blood.objects.all()
        serializer=bloodSerializer(blood1,many=True)
        return Response(serializer.data)

    def post(self):
        pass


class hospitalList(APIView):

    def get(self,request):
        hospital1=hospital.objects.all()
        serializer=hospitalSerializer(hospital1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class bloodBankList(APIView):

    def get(self,request):
        bloodBank1=bloodBank.objects.all()
        serializer=bloodBankSerializer(bloodBank1,many=True)
        return Response(serializer.data)

    def post(self):
        pass


class EmployeeList(APIView):

    def get(self,request):
        Employee1=Employee.objects.all()
        serializer=EmployeeSerializer(Employee1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class ordersList(APIView):

    def get(self,request):
        orders1=orders.objects.all()
        serializer=ordersSerializer(orders1,many=True)
        return Response(serializer.data)

    def post(self):
        pass












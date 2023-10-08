from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect

from customer.models import Customer
from customer.models import Students
from customer.serializers import CustomerSerializer, StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

def customers(request):
    # invoke serializer and return to client

    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse({'customers': serializer.data})


@api_view(['GET', 'POST', 'DELETE'])
def Customerdetails(request, id):
    try:
        data = Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        return redirect("/")
    serializer = CustomerSerializer(data)
    return JsonResponse({'customer': serializer.data})


def students(request):
    # invoke serializer and return to client
    data = Students.objects.all()
    serializer = StudentSerializer(data, many=True)
    return JsonResponse({'students': serializer.data})


def studentdetails(request, id):
    try:
        data = Students.objects.get(id=id)
    except Students.DoesNotExist:
        return redirect("/")
    serializer = StudentSerializer(data)
    return JsonResponse({'student': serializer.data})

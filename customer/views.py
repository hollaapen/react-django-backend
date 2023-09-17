from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from customer.models import Customer
from customer.serializers import CustomerSerializer


# Create your views here.

def customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse({'customers':serializer.data})


def details(request, id):
    data = Customer.objects.get(id=id)
    serializer = CustomerSerializer(data)
    return JsonResponse({'customer':serializer.data})


















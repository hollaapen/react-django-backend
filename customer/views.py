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

# def Customerdetails(request, id):
#     try:
#         data = Customer.objects.get(id=id)
#     except Customer.DoesNotExist:
#         return redirect("/")
#     serializer = CustomerSerializer(data)
#     return JsonResponse({'customer': serializer.data})


@api_view(['GET', 'POST'])
def customers(request):
    # invoke serializer and return to client
    if request.method == 'GET':
        data = Customer.objects.all()
        serializer = CustomerSerializer(data, many=True)
        return Response({'customers': serializer.data})

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'customer': serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def Customerdetails(request, id):
    try:
        data = Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(data)
        return Response({'customer': serializer.data})

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




    elif request.method == 'POST':

        serializer = CustomerSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'customer': serializer.data})
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


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

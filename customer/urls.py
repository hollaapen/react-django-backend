from django.urls import path
from . import views

urlpatterns = [

    path('api/customers', views.customers, name="customers"),
    path('api/customers/<id>', views.details, name="details")

]

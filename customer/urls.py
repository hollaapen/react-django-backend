from django.urls import path
from customer import views

urlpatterns = [

    path('api/customers/', views.customers, name="customers"),
    path('api/customers/<int:id>', views.Customerdetails, name="details"),


]

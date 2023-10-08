from django.urls import path
from customer import views

urlpatterns = [

    path('api/customers/', views.customers, name="customers"),
    path('api/customers/<int:id>', views.Customerdetails, name="details"),
    path('api/students', views.students, name="students"),
    path('api/students/<int:id>', views.studentdetails, name="studentdetails")


]

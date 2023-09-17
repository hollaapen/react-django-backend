from rest_framework import serializers
from customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

        # install django cors headers
        # pip install django-cors-headers
#         add it into installed apps and middlewares

# create a list of allowed origins in the settings file


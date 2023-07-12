from rest_framework import serializers
from .models import School


class SchoolSerializer(serializers.ModelSerializer):
    """
       Serializer class used in DRF to convert objcet into bytes
    """

    class Meta:
        """
             meta class is used to change the behaviour of the model fields
        """
        model = School
        fields = ['id', 'name', 'address', 'pincode', 'latitude', 'longitude']

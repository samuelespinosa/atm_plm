from rest_framework import serializers
from .models import *  
class ProcessAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProcessAssignment
        fields=("process","employee")

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process 
        fields = (
            "date_in",
            "date_out",
            "date_start",
            "state",
        )

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer 
        fields = (
            "name",
            "last_name",
            "process",
        )
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer 
        fields = (
            "name",
            "city",
            "email",
            "country",
        )

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill 
        fields = (
            "amount",
            "state",
        )

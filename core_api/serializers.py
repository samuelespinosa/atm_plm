from rest_framework import serializers
from .models import *  
class ProcessAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProcessAssignment
        fields=("process","developer")

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process 
        fields = (
            "date_in",
            "date_out",
            "date_start",
            "state",
        )

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee 
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

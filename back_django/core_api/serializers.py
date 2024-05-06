from rest_framework import serializers
from .models import *  

class ProcessAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProcessAssignment
        fields='__all__'

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process 
        fields='__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance) 
        representation["bill"] = {'id':instance.bill.id, 'amount':instance.bill.amount}
        developers=UserSerializer(instance.developer.all(),many=True).data 
        representation['developer']=[{'id':developer.get('id'),'name':f'{developer.get("first_name")} {developer.get("last_name")}'} for developer in developers] 
        representation["customer"] = {'id':instance.customer.id, 'name':' '.join((instance.customer.first_name,instance.customer.last_name))}
        return representation       
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', ) 

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee 
        fields = '__all__'
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer 
        fields = '__all__' 
        
class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill 
        fields = '__all__'

class MonthlyBillSummarySerializer(serializers.Serializer):
    total_amount_paid = serializers.DecimalField(max_digits=10, decimal_places=2)
    bills = BillSerializer(many=True)


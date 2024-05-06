from rest_framework import generics,permissions,views,status, viewsets
from .models import * 
from .serializers import * 
from .permissions import IsDeveloperOrReadOnly
from datetime import date, timedelta, datetime,time
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum 
from django.db.models.functions import TruncMonth,TruncYear

class MeView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class BillViewSet(viewsets.ModelViewSet):
    queryset= Bill.objects.all()
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class=BillSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.queryset 
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def get_filtered_query_set(self):
        return self.queryset.annotate(month=TruncMonth('created_at'))\
        .annotate(year=TruncYear('created_at'))\
        .values('month','year')\
        .annotate(sum_amount=Sum('amount'))
    
    @action(detail=False)
    def month_sumary(self, request):
        queryset=self.get_filtered_query_set()
        bills_list = [
            {
                'year': item['year'].strftime('%Y'),
                'month': item['month'].strftime('%m'), 
                'sum_amount': item['sum_amount']
            }
            for item in queryset 
        ]

        return Response(bills_list)


class ProcessList(generics.ListCreateAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsDeveloperOrReadOnly,
    ) 

class CustomerSearchView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        name=self.request.GET.get('name','');
        queryset=Customer.objects.all()
        if name: 
            queryset=Customer.objects.filter(name__icontains=name)
        return queryset
    def get(self,request):
        queryset=self.get_queryset()
        serializer=CustomerSerializer(customers)
        return Response(serializer.data)

class ProcessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer


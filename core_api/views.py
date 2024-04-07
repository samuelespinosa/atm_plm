from rest_framework import generics
from .models import * 
from .serializers import * 


class ProcessList(generics.ListCreateAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer


class ProcessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

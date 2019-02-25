from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StockDetail
from .serializers import StockDetailSerializer
from rest_framework import generics,permissions
class StockList(generics.CreateAPIView):
    serializer_class = StockDetailSerializer
    queryset = StockDetail.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self,request):
        stocks = StockDetail.objects.all()
        serializer = StockDetailSerializer(stocks,many = True)
        return Response(serializer.data)


def stock(request):
    return HttpResponse('Hello world')

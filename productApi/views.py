from functools import partial
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from productApi.serializers import CustomerSerializer, ProductSerializer
from .models import Customer, Product
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,DjangoModelPermissions
from rest_framework import viewsets


# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated,IsAdminUser]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer




class CustomerViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated,IsAdminUser]
    permission_classes=[DjangoModelPermissions]

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer



# class ProductViewSet(ViewSet):
#     authentication_classes=[BasicAuthentication]
#     permission_classes=[IsAuthenticated  ]


#     def list(self,request):
#         prod  = Product.objects.all()
#         serializer = ProductSerializer(prod,many=True)
#         return Response(serializer.data)


#     def retrieve(self,request,pk):
#         try:
#             prod = Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             return Response(status=Http404)

#         serializer = ProductSerializer(prod)
#         return Response(serializer.data)


#     def create(self,request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



#     def update(self,request,pk):
#         try:
#             prod = Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             return Response(status=Http404)

#         serializer = ProductSerializer(prod,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Updated'})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#     def partial_update(self,request,pk):
#         try:
#             prod = Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             return Response(status=Http404)

#         serializer = ProductSerializer(prod,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Updated'})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self,request,pk):
#         try:
#             prod = Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             return Response(status=Http404)

#         prod.delete()
#         return Response({'msg':'Data Deleted'})


from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from employeeApi import serializers
from employeeApi.models import Employee,Project
from employeeApi.serializers import EmployeeSerializer,ProjectSerializer

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def Employee_list(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)

        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def Employee_detail(request,pk):
    try:
        emp = Employee.objects.get(pk = pk)

    except Employee.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = EmployeeSerializer(emp)
        return JsonResponse(serializer.data)

    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(emp,data = data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)

        return JsonResponse(serializer.errors,status=400)

    
    elif request.method == 'DELETE':
        emp.delete()
        return HttpResponse(status = 204) 
        #204 no content success status response code - indicates request fulfilled but need not navigate from current page


@csrf_exempt
def Project_list(request):
    if request.method == 'GET':
        proj = Project.objects.all()
        serializer = ProjectSerializer(proj,many =True)
        return JsonResponse(serializer.data,safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        
        return JsonResponse(serializer.errors,status = 400)


@csrf_exempt
def Project_detail(request,pk):
    try:
        proj = Project.objects.get(pk=pk)

    except Project.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = ProjectSerializer(proj)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(proj,data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)

        return JsonResponse(serializer.errors,status = 400)

    elif request.method == 'DELETE':
        proj.delete()
        return HttpResponse(status = 204) 


from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from employeeApi.models import Employee,Project
from employeeApi.serializers import EmployeeSerializer,ProjectSerializer

from django.views.decorators.csrf import csrf_exempt


# function to handle get and post for employee 
@csrf_exempt
def Employee_list(request):
    if request.method == 'GET':
        employee = Employee.objects.all()       # getting all employees record from DB
        serializer = EmployeeSerializer(employee,many=True)     #serializing it
        return JsonResponse(serializer.data,safe=False)     # returns list of employee in Json format
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)          # parsing incoming data 
        serializer = EmployeeSerializer(data = data)        #deserializing parsed data
        
        if serializer.is_valid():   # checks for validation errors
            serializer.save()       # creating new employee record
            return JsonResponse(serializer.data,status = 201)   # creates newly created employee as a Json object

        return JsonResponse(serializer.errors,status=400)       # returns errors in serializers if any or returns bad request error



# function to handle get, put, post and delete requests for a particular employee id
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
        




# function to handle get and post for Project Model
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


# function to handle get, put, post and delete requests for a particular project
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


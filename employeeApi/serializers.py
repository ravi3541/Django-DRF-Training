from rest_framework import serializers
from employeeApi.models import Employee, Project
import re


# employee Serializer
class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    ename = serializers.CharField(required = True, max_length = 30)
    designation = serializers.CharField(max_length =50)
    addr = serializers.CharField(max_length = 100)
    salary = serializers.IntegerField()


    def create(self,validated_data):
        return Employee.objects.create(**validated_data)

    
    def update(self,instance, validated_data):
        instance.ename = validated_data.get('ename',instance.ename)
        instance.designation = validated_data.get('designation',instance.designation)
        instance.addr = validated_data.get('addr',instance.addr)
        instance.salary = validated_data.get('salary',instance.salary)

        instance.save()

        return instance

    
    #validation for employee name 
    def validate_ename(self,value):
        if len(value)>=3:
            if re.findall('^[a-zA-Z\s]*$',value):
               
                return value
             
            raise serializers.ValidationError('Name can only contain alphabets')

        raise serializers.ValidationError("Minimum 3 characters required")


    #validation for employee designation 
    def validate_designation(self,value):
        if len(value)>=2:
            if re.findall('^[a-zA-Z\s]*$',value):
                
                return value
             
            raise serializers.ValidationError('Only Alphabets allowed')

        raise serializers.ValidationError("Minimum 2 characters required")


    #validation for employee salary 
    def validate_salary(self,value):
        if value > 8000:
            return value
             
        raise serializers.ValidationError("Salary cannot be less than 8000")




# Model serializer for Project model
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','title','desc','deadline','emp']
        depth = 1

        
    
   
from rest_framework import serializers
from employeeApi.models import Employee, Project
import re

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

    
    def validate_ename(self,value):
        if len(value)>=3:
            if re.findall('^[a-zA-Z\s]*$',value):
                # print("Valid ")
                return value
            # print("Invalid") 
            raise serializers.ValidationError('Name can only contain alphabets')

        raise serializers.ValidationError("Minimum 3 characters required")


    def validate_designation(self,value):
        if len(value)>=2:
            if re.findall('^[a-zA-Z\s]*$',value):
                # print("Valid ")
                return value
            # print("Invalid") 
            raise serializers.ValidationError('Only Alphabets allowed')

        raise serializers.ValidationError("Minimum 2 characters required")


    def validate_salary(self,value):
        if value > 8000:
            return value
             
        raise serializers.ValidationError("Salary cannot be less than 8000")




class ProjectSerializer(serializers.ModelSerializer):
    #team = EmployeeSerializer(many = True,read_only = True)# this line is not working
    class Meta:
        model = Project
        fields = ['id','title','desc','deadline','emp']

        
    
   
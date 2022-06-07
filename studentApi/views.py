from lib2to3.pgen2.pgen import generate_grammar
from venv import create
from django.shortcuts import render
from rest_framework import generics,mixins
from .models import *
from .serializers import *


# Generic View for Student List
class StudentList(generics.ListAPIView,generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class =StudentSerializer

# Generic View for Student Detail
class StudentDetail(generics.UpdateAPIView,generics.DestroyAPIView,generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class =StudentSerializer
    lookup_field = 'pk'



# Course List class using mixins
class CourseList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


# Course Detail class using mixins
class CourseDetail(mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
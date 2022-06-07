# Implementataion of Function based and Class Based Views
  
from django.shortcuts import render
from songsalbumApi.models import Singer
from songsalbumApi.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404


# Function Based View for Singer Model 

# Function to handle get and post request for Singer Model
@api_view(['GET','POST'])
def Singer_list(request):
    if request.method == 'GET':
        singer = Singer.objects.all()      
        serializer = SingerSerializer(singer,many=True)     
        return Response(serializer.data)       
    
    elif request.method == 'POST':
        serializer = SingerSerializer(data=request.data)    
        if serializer.is_valid():     
            serializer.save()           
            return Response(serializer.data,status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      


# function to handle put, patch, get and delete request for a particular singer id
@api_view(['GET','PUT','DELETE','PATCH'])
def Singer_detail(request,pk):
    try:
        singer = Singer.objects.get(pk=pk)     
    except Singer.DoesNotExist:                
        return Response(status=status.HTTP_404_NOT_FOUND)       

    if request.method=='GET':               
        serializer = SingerSerializer(singer)       
        return Response(serializer.data)            

    elif request.method == 'PUT':           
        serializer =SingerSerializer(singer,data=request.data)      
        if serializer.is_valid():      
            serializer.save()           
            return Response(serializer.data)    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)       


    elif request.method == 'PATCH':         
        serializer =SingerSerializer(singer,data=request.data)      
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



    elif request.method == 'DELETE':
        singer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






# CLass Based View for Song Model
# class for handling get and post request 
class SongList(APIView):

    def get(self, request, format=None):
        song = Song.objects.all()
        serializer = SongSerializer(song,many=True)
        return Response(serializer.data)        
        
    
    def post(self, request, format=None):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class to handle get, put, patch and delete request 
class SongDetail(APIView):
    def get_object(self,pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

  
    def get(self,request,pk,format=None):
        song = self.get_object(pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)



    def put(self,request,pk,format=None):
        song = self.get_object(pk)
        serializer =SongSerializer(song,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def patch(self,request,pk,format=None):
        song = self.get_object(pk)
        serializer =SongSerializer(song,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



    def delete(self,request,pk,format=None):
        song = self.get_object(pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






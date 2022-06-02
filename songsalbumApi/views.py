from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from songsalbumApi.models import Singer
from songsalbumApi.serializers import *
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def Singer_list(request):
    if request.method == 'GET':
        singer = Singer.objects.all()
        serializer = SingerSerializer(singer,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        print("in POST")
        serializer = SingerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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



@api_view(['GET','POST'])
def Song_list(request):
    if request.method == 'GET':
        song = Song.objects.all()
        serializer = SongSerializer(song,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        print("in POST")
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE','PATCH'])
def Song_detail(request,pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer =SongSerializer(song,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'PATCH':
        serializer =SongSerializer(song,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

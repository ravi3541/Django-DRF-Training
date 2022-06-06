from .models import *
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class SingerSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True,read_only=True)

    class Meta:
        model = Singer
        fields = ['id','name','gender','age','city','songs']


from rest_framework import serializers
from .models    import Project  

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','nombre','descripcion','precio','disponible')
        
    
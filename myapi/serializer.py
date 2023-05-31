from rest_framework import serializers
from .models import Usuario
from .models import Post
from .models import UsuarioPost 

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'sobrenome', 'username', 'email', 'senha')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ('id', 'postagem', 'data_hora', 'username')

class UsuarioPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPost
        fields = ('usuario','post')                

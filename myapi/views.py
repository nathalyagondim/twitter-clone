from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializer import PostSerializer
from .models import Usuario
from .serializer import UsuarioSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView


class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostretrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer     

class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioretrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class FeedGeralView(APIView):
    pagination_class = PageNumberPagination

    def get(self, request):
        # Obtenha todos os posts ordenados pela data_hora em ordem decrescente
        posts = Post.objects.order_by('-data_hora')

        # Configure a paginação
        paginator = self.pagination_class()
        paginated_posts = paginator.paginate_queryset(posts, request)

        # Serialize os posts paginados
        serializer = PostSerializer(paginated_posts, many=True)

        # Retorne os posts paginados no formato JSON
        return paginator.get_paginated_response(serializer.data)

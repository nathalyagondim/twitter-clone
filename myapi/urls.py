from django.urls import path 
from .views import PostListCreate, PostretrieveUpdateDelete
from .views import UsuarioListCreate, UsuarioretrieveUpdateDelete, FeedGeralView

urlpatterns = [
    path('posts', PostListCreate.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostretrieveUpdateDelete.as_view(), name='post-details'),
    path('usuarios', UsuarioListCreate.as_view(), name='usuario-list'),
    path('usuario/<int:pk>/', UsuarioretrieveUpdateDelete.as_view(), name='usuario-details'),
    path('feed-geral/', FeedGeralView.as_view(), name='feed-geral'),
]

from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    postagem = models.TextField(max_length=280)
    data_hora = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=255)

    def __str__(self):
        return f"postagem: {self.postagem}, data: {self.data_hora}"


class UsuarioPost(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
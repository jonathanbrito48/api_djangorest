from django.db import models
import hashlib
import secrets
from django.contrib.auth.models import AbstractBaseUser

class clientes(models.Model):
    client_name = models.CharField(max_length=100,blank=False,null=False)
    api_token = models.CharField(max_length=32, unique=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    @property
    def is_authenticated(self):
        """Sempre retorna True para clientes existentes"""
        return True

    def save(self,*args, **kwargs):
        if not self.id:
            self.id = secrets.token_hex(16)
        if not self.api_token:
            self.api_token = hashlib.md5(secrets.token_hex(16).encode()).hexdigest()
        super().save(*args,**kwargs)

    def __str__(self):
        return str(self.client_name)

class lojas(models.Model):
    client = models.ForeignKey(clientes,on_delete=models.CASCADE,editable=False)
    Loja= models.CharField(max_length=100)
    Endereco = models.CharField(max_length=100)
    Bandeira = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.client_id)
from django.db import models
import hashlib
import secrets
from django.contrib.auth.models import AbstractBaseUser


class empresa(models.Model):
    client_name=models.CharField(max_length=100,blank=False,null=False)
    api_token=models.CharField(max_length=43, unique=True,editable=False)
    created_at=models.DateTimeField(auto_now_add=True)
    ativo=models.BooleanField(default=True)

    @property
    def is_authenticated(self):
        return True

    def save(self,*args, **kwargs):
        if not self.api_token:
            self.api_token = hashlib.md5(secrets.token_hex(16).encode()).hexdigest()
        super().save(*args,**kwargs)

    def __str__(self):
        return str(self.client_name)


class integration(models.Model):
    empresa=models.ForeignKey(empresa,on_delete=models.CASCADE,editable=False)
    id_venda_item=models.AutoField(primary_key=True,unique=True,auto_created=True,blank=False,null=False)
    id_venda=models.CharField(max_length=100,blank=False,null=False)
    data_venda=models.DateField(null=False,blank=False)
    data_envio=models.DateField(null=False,blank=False)
    tipo_envio=models.CharField(max_length=100)
    id_cliente=models.CharField(max_length=100,blank=False,null=False)
    nome_cliente=models.CharField(max_length=100,blank=False,null=False)
    segmento=models.CharField(max_length=100,blank=False,null=False)
    pais=models.CharField(max_length=100,blank=False,null=False)
    cidade=models.CharField(max_length=100,blank=False,null=False)
    estado=models.CharField(max_length=100,blank=False,null=False)
    codigo_postal=models.CharField(max_length=100,blank=False,null=False)
    regiao=models.CharField(max_length=100,blank=False,null=False)
    id_produto=models.CharField(max_length=200,blank=False,null=False)
    descricao_produto=models.CharField(max_length=500,null=False,blank=False)
    categoria_produto=models.CharField(max_length=200,null=False,blank=False)
    subcategoria_produto=models.CharField(max_length=200,null=False,blank=False)
    valor_venda=models.DecimalField(decimal_places=2,max_digits=2,null=False,blank=False)
    quantidade_vendida=models.DecimalField(decimal_places=2,max_digits=2,null=False,blank=False)
    desconto=models.DecimalField(decimal_places=2,max_digits=2,null=False,blank=False)
    margem=models.DecimalField(decimal_places=2,max_digits=2,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_venda_item)
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


class dim_cliente(models.Model):
    empresa=models.ForeignKey(empresa,on_delete=models.CASCADE,editable=False)
    id_cliente=models.CharField(max_length=100,primary_key=True,unique=True,blank=False,null=False)
    nome_cliente=models.CharField(max_length=100,blank=False,null=False)
    segmento=models.CharField(max_length=100,blank=False,null=False)
    pais=models.CharField(max_length=100,blank=False,null=False)
    cidade=models.CharField(max_length=100,blank=False,null=False)
    estado=models.CharField(max_length=100,blank=False,null=False)
    codigo_postal=models.CharField(max_length=100,blank=False,null=False)
    regiao=models.CharField(max_length=100,blank=False,null=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_client)
    

class dim_produto(models.Model):
    empresa=models.ForeignKey(empresa,on_delete=models.CASCADE,editable=False)
    id_produto=models.CharField(max_length=100,primary_key=True,unique=True,blank=False,null=False)
    produto=models.CharField(max_length=200,blank=False,null=False)
    categoria=models.CharField(max_length=100,blank=False,null=False)
    sub_categoria=models.CharField(max_length=100,blank=False,null=False)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.produto)
    

class dim_tempo_venda(models.Model):
    empresa=models.ForeignKey(empresa,on_delete=models.CASCADE,editable=False,blank=False,null=False)
    id_data_venda=models.CharField(max_length=100,unique=True,primary_key=True,blank=False,null=False)
    data_venda=models.DateField(blank=False,null=False)
    dia_venda=models.IntegerField(editable=False)
    mes_venda=models.IntegerField(editable=False)
    ano_venda=models.IntegerField(editable=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        self.dia_venda = self.data_venda.day
        self.mes_venda = self.data_venda.month
        self.ano_venda = self.data_venda.year
        super().save(*args,**kwargs)

    def __str__(self):
        return str(self.data_venda)
    

class dim_tempo_entrega(models.Model):
    empresa=models.ForeignKey(empresa,on_delete=models.CASCADE,editable=False,blank=False,null=False)
    id_data_entrega=models.CharField(max_length=100,unique=True,primary_key=True,blank=False,null=False)
    data_entrega=models.DateField(blank=False,null=False)
    dia_entrega=models.IntegerField(blank=False,null=False)
    mes_entrega=models.IntegerField(blank=False,null=False)
    ano_entrega=models.IntegerField(blank=False,null=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        self.dia_entrega = self.data_entrega.day
        self.mes_entrega = self.data_entrega.month
        self.ano_entrega = self.data_entrega.year
        super().save(*args,**kwargs)

    def __str__(self):
        return str(self.data_entrega)


class dim_tipo_entrega(models.Model):
    empresa=models.ForeignKey(empresa,on_delete=models.CASCADE,editable=False,blank=False,null=False)
    id_tipo_entrega=models.CharField(null=False,blank=False,primary_key=True,unique=True)
    tipo_entrega=models.CharField(max_length=100,blank=False,null=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.tipo_entrega)
    

class fato_vendas(models.Model):
    empresa=models.ForeignKey(empresa,on_delete=models.CASCADE,editable=False,blank=False,null=False)
    id_venda_item=models.CharField(null=False,blank=False,unique=True,primary_key=True)
    venda=models.CharField(null=False,blank=False)
    produto=models.ForeignKey(dim_produto,on_delete=models.CASCADE,editable=False,blank=False,null=False)
    cliente=models.ForeignKey(dim_cliente,on_delete=models.CASCADE,editable=False,blank=False,null=False)
    data_venda=models.ForeignKey(dim_tempo_venda,on_delete=models.CASCADE,editable=False,blank=False,null=False)
    data_entrega=models.ForeignKey(dim_tempo_entrega,on_delete=models.CASCADE,editable=False,blank=False,null=False)
    tipo_entrega=models.ForeignKey(dim_tipo_entrega,on_delete=models.CASCADE,editable=False,blank=False,null=False)
    quantidade=models.DecimalField(null=False,blank=False,max_digits=10,decimal_places=2)
    venda_valor=models.DecimalField(null=False,blank=False,max_digits=10,decimal_places=2)
    desconto=models.DecimalField(null=False,blank=False,max_digits=10,decimal_places=2)
    margem=models.DecimalField(null=False,blank=False,max_digits=10,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_venda_item)

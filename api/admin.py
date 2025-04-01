from django.contrib import admin
from django.db import models
from .models import clientes,lojas

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('id','client_name','api_token','created_at')

admin.site.register(clientes,ClientesAdmin)

class LojasAdmin(admin.ModelAdmin):
    list_display = ('id','client')

admin.site.register(lojas,LojasAdmin)



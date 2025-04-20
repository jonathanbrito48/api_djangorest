from django.contrib import admin
from django.db import models
from .models import empresa

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id','client_name','api_token','created_at','ativo')
    list_editable = ('ativo',)

admin.site.register(empresa,EmpresaAdmin)
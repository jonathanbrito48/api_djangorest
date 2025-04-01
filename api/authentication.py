from rest_framework import authentication
from rest_framework import exceptions
from .models import clientes
import hashlib

class MD5TokenAuthentication(authentication.BaseAuthentication):
    keyword = 'Token'

    def authenticate(self, request):
        auth = authentication.get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None
        
        if len(auth) == 1:
            raise exceptions.AuthenticationFailed('Token inválido. Credenciais não fornecidas.')
        elif len(auth) > 2:
            raise exceptions.AuthenticationFailed('Token inválido. Token não deve conter espaços.')
        
        try:
            token = auth[1].decode()
            cliente = clientes.objects.get(api_token=token,ativo=True)
        except clientes.DoesNotExist:
            raise exceptions.AuthenticationFailed('Token inválido. Cliente não encontrado ou inativo')

        return (cliente,None) 
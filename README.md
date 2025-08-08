# API Django REST

Este projeto é uma API desenvolvida com Django e Django REST Framework, focada em integração entre sistemas. Ela fornece endpoints para recebimento de dados, permitindo apenas operações de criação (POST).

## Descrição

A API foi projetada exclusivamente para integração, aceitando apenas requisições POST para criação de registros. Cada requisição autenticada tem o id do usuário autenticado registrado automaticamente no modelo de integração, garantindo rastreabilidade e segurança.

## Vantagens

- **Foco em integração**: Ideal para conectar sistemas externos de forma segura e controlada.
- **Apenas POST**: Operações restritas a criação de dados, evitando alterações ou exclusão acidental.
- **Autenticação obrigatória**: Apenas usuários autenticados podem enviar dados.
- **Registro do usuário**: O id do usuário autenticado é gravado automaticamente em cada integração.
- **Documentação automática**: Endpoints documentados via Swagger/OpenAPI.
- **Validação de dados robusta**: Utiliza serializers do Django REST Framework.
- **Extensível**: Fácil de adicionar novos campos ou integrações.

## Requisitos

- Python 3.8+
- Django 3.2+
- Django REST Framework
- Docker e Docker Compose (para o banco de dados PostgreSQL)

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/jonathanbrito48/api_djangorest.git
   cd api_djangorest
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
   - Copie o arquivo `.env.example` para `.env` (ou crie um novo `.env`) na raiz do projeto com o seguinte conteúdo:
     ```env
     POSTGRES_DB='api_django'
     POSTGRES_USER='api_django'
     DB_PASSWORD='sua_senha'
     HOST='localhost'
     ```
   - Ajuste os valores conforme necessário.

5. Suba o banco de dados PostgreSQL com Docker Compose:
   ```bash
   docker-compose up -d
   ```

6. Realize as migrações:
   ```bash
   python manage.py migrate
   ```

7. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

## Autenticação

A API utiliza autenticação baseada em tokens, garantindo que apenas usuários autenticados possam enviar dados.

- **Token Authentication**: Após criar um usuário, obtenha um token de acesso via endpoint `/api/token/` (ou similar).

Exemplo de uso do token em requisições:
```http
Authorization: Token seu_token_aqui
```

> **Importante:** O id do usuário autenticado é registrado automaticamente no modelo de integração a cada requisição POST.

## Exemplos de Endpoints

- `POST /api/integrations/` — Cria um novo registro de integração (requer autenticação).

Exemplo de requisição:
```http
POST /api/integrations/
Authorization: Token seu_token_aqui
Content-Type: application/json

{
  "campo1": "valor",
  "campo2": "valor"
}
```
A resposta incluirá o id do usuário autenticado associado ao registro.

## Uso

Acesse `http://localhost:8000/` para utilizar a API. Consulte a documentação dos endpoints no arquivo `docs` ou via navegação no navegador.

A documentação interativa (Swagger ou Redoc) pode ser acessada em:
- `http://localhost:8000/docs/`
- `http://localhost:8000/swagger/`

## Testes

Para rodar os testes automatizados:
```bash
python manage.py test
```

## Contribuição

Contribuições são bem-vindas! Abra uma issue ou envie um pull request.

## Licença

Este projeto está sob a licença MIT.
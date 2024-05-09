# API da Biblioteca Django 📚
<p align="justify">
Esta é uma API REST em Django para gerenciar um sistema de biblioteca. Ela permite realizar várias operações relacionadas a autores e livros, incluindo criação, atualização e exclusão de registros, bem como a importação de autores de um arquivo CSV.
</p>

## Funcionalidades

- **Lista de Autores**: Endpoint para listar todos os autores.
  - URL: `/authors/`
  - Método: GET

- **Lista de Livros**: Endpoint para listar todos os livros ou criar um novo livro.
  - URL: `/books/`
  - Método: GET, POST

- **Lista de Livros Personalizada**: Endpoint personalizado para filtrar livros por nome, ano de publicação, edição ou autor.
  - URL: `/custom-books/`
  - Método: GET

- **Detalhes do Livro**: Endpoint para recuperar, atualizar ou excluir um livro específico pelo seu ID.
  - URL: `/books/<int:pk>/`
  - Método: GET, PUT, DELETE

## Tecnologias

- [Django](https://www.djangoproject.com/)
- [Django REST Framework (DRF)](https://www.django-rest-framework.org/)
- [SQLite](https://www.sqlite.org/)
- [Python](https://www.python.org/)
 
Outras dependências estão listadas no arquivo `requirements.txt`.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/iajor/api-biblioteca-django.git
   ```

2. Instale os pacotes necessários:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute as migrações para criar o esquema do banco de dados:

   ```bash
   python manage.py migrate
   ```

4. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

## Importando Autores de um CSV

Para importar autores de um arquivo CSV, você pode usar o seguinte comando de gerenciamento:

```bash
python manage.py import_author author.csv
```

## Executando Testes

Para executar os testes automatizados, execute o seguinte comando:

```bash
python manage.py test
```

## Contribuidores

- André Rojai (@rojaiandre)

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

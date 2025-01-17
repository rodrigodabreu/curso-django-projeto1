# Desenvolvimento WEB com Python, Django e Django REST Framework

### Criando o ambiente virtual

```
python -m venv venv
```

### Ativando o ambiente virtual

```
. venv/bin/activate
```

### Instalando o Django

```
pip install django
```

### Instalando o Django REST Framework

```
pip install djangorestframework
```

### Criando o projeto

```
django-admin startproject api .
```

### Criando a aplicação

```
python manage.py startapp core
```

### Instalando as dependências

```
pip install -r requirements.txt
```

### Criando as migrações

```
python manage.py makemigrations
```

### Executando as migrações

```
python manage.py migrate
```

### Criando um super usuário

```
python manage.py createsuperuser
```

### Executando o servidor

```
python manage.py runserver
```

### Acessando o admin

```
http://localhost:8000/admin/
```

### Acessando a API

```
http://localhost:8000/api/
```

### Acessando a documentação da API

```
http://localhost:8000/api/docs/
```

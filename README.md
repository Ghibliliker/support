[![Django-support workflow](https://github.com/Ghibliliker/support/actions/workflows/support.yml/badge.svg?branch=main&event=push)](https://github.com/Ghibliliker/support/actions/workflows/support.yml)

#  Test task "Support"

###  About project:

Support - implementation of helpdesk, users with problems can ask for help, supports see created requests and can respond to them, as a result, supports can change the status of the request. When the request status changes, a message is sent to the user's mail

### Technology stack
```
Python 3
Django
Django REST Framework
JWT
PostgreSQL
PyTest
Docker
Celery
Redis
```

## How to start a project:
 
 1. Download a project
 2. Install docker, docker-compose
 3. Create .env with these constants 
 ```
DB_ENGINE=***
DB_NAME=***
POSTGRES_USER=***
POSTGRES_PASSWORD=***
DB_HOST=***
DB_PORT=***
SECRET_KEY=***
EMAIL_HOST=***
EMAIL_PORT=***
EMAIL_HOST_USER=***
EMAIL_HOST_PASSWORD=***
EMAIL_USE_TLS=***
EMAIL_USE_SSL=***
```
4. Building and running a container
```
docker-compose up -d --build
```
5. Migrations
```
docker-compose exec support python manage.py makemigrations
docker-compose exec support python manage.py migrate
```
7. Collection of static files
```
docker-compose exec support python manage.py collectstatic --noinput
```
8. Creating a superuser
```
docker-compose exec support python manage.py createsuperuser
```

## Testing:

Project testing implemented via GitHub Actions:
When pushing, the code is automatically checked by flake8

## API documentation:

Documentation implemented through auto-generation

Swagger documentation
```
localhost/swagger/
```
ReDoc documentation
```
localhost/redoc/
```

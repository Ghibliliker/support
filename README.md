[![Django-support workflow](https://github.com/Ghibliliker/support/actions/workflows/support.yml/badge.svg?branch=main&event=push)](https://github.com/Ghibliliker/support/actions/workflows/support.yml)

#  Тестовое задание "Служба поддержкиn"

###  О чем проект:

Служба Поддержки - реализация службы поддержки, пользователи с проблемами могут обращаться за помощью, служба поддержки видит созданные запросы и может отвечать на них, в результате, может изменить статус запроса. При изменении статуса запроса на почту пользователя приходит сообщение

### Стек технологий
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

## Как запустить проект:
 
 1. Скачать проект
 2. Установить docker, docker-compose
 3. Создать .env с нижепредставленными переменными
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
4. Сборка и запуск контейнера
```
docker-compose up -d --build
```
5. Миграции
```
docker-compose exec support python manage.py makemigrations
docker-compose exec support python manage.py migrate
```
7. Сбор статики
```
docker-compose exec support python manage.py collectstatic --noinput
```
8. Создание суперпользователя Django
```
docker-compose exec support python manage.py createsuperuser
```

## Тестирование:

Тестирование проекта реализовано через GitHub Actions:
При push код автоматически проверяется flake8, запускается pytest 

## Эндпоинты, поддерживаемые API:

* POST /api/auth/users/    Регистрация нового пользователя
```
{
    "username": "string",
    "password": "string",
    "email": "string@mail",
    "first_name": "string",
    "last_name": "string"
}
```
* GET/PATCH /api/auth/users/me    Получить/обновить пользователя
* POST /api/auth/jwt/create    Получение JWT-токена
```
{
    "password": "string",
    "email": "string@mail"
}
```
* POST /api/auth/jwt/refresh    Получение нового JWT-токена по истечению жизни старого
* GET/POST /api/v1/tickets/    Создание/получение списка тикетов
```
{
    "name": "string",
    "text": "string",
    "image": image
}
```
* GET/PATCH/DELETE /api/v1/tickets/{tickets_id}/    Получение/изменение/удаление тикета
* PATCH /api/v1/tickets/{tickets_id}/status    Обновление статуса тикета(только саппорт)
```
{
    "status": "string"
}
```
* GET/POST /api/v1/tickets/{tickets_id}/comments/    Добавления комментария к тикету/получение всех комментариев
```
{
    "text": "string",
    "image": image
}
```
* GET/PATCH/DELETE /api/v1/tickets/{tickets_id}/comments/{comments_id}/    Получение/изменение/удаление комментария


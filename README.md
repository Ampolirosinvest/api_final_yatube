# API_Yatube

REST API для социальной сети блогеров Yatube.

## Характеристики

Аутентификация по JWT-токену
Работает со всеми модулями социальной сети Yatube: постами, комментариями, группами, подписчиками
Получение полного списка всех сообщений на Yatube
Получение списка сообщений, принадлежащих определенной группе
Получение полного списка комментариев ко всем постам
Получение списка комментариев к конкретному посту
Возможность подписки и отписки от автора
Поддерживает методы GET, POST, PUT, PATCH, DELETE
Предоставляет данные в формате JSON

## Стек технологий

- Django REST Framework - написание проекта на Python
- Simple JWT - работа с JWT-токеном
- Git - управление версиями

## Запуск проекта

1) Необходимо склонировать репозитарий проекта:
```
git clone https://github.com/Ampolirosinvest/api_final_yatube.git
```
2) Установить и активировать виртуальное окружение:
```
python -m venv venv
sourse venv/Scripts/activate
```
3) Установить необходимые зависимости:
```
pip install -r requirements.txt
```
4) Выполните миграции:
```
python manage.py makemigrations
python manage.py migrate
```
5) Создайте суперпользователя:
```
python manage.py createsuperuser
```

6) Запустите сервер:
```
python manage.py runserver
```
Ваш проект запустился на http://127.0.0.1:8000/
С помощью команды *pytest* вы можете запустить тесты и проверить работу модулей
C помощью *flake8* вы можете проверить оформление кода

7) Можно создать пользователя после запуска проекта:
```
http://127.0.0.1:8000/api/v1/users/
```
отправить запрос:
    {
        "username": "XXXXX",
        "password": "XXXXX"
    }

## Аутентификация

Выполните POST-запрос *localhost:8000/api/v1/jwt/create/* передав поля username и password(см. пункт 7).

API вернет JWT-токен в формате:

    {
        "refresh": "ХХХХХ",
        "access": "ХХХХХ"
    }
    
access - наш токен, который необходимо передать в заголовке Authorization: Bearer <токен> при отправке запросов
refresh - необходим для обновления токена

Запрос на refresh тонека - POST запрос *localhost:8000/api/v1/jwt/create/* в формате:
    
    {
    "username": "XXXXX",
    "password": "XXXXX",
    "refresh": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    }


## Примеры запросов и ответов

POST запрос на `/api/v1/posts`:

```
{
    "text": "Привет МИР!"
}
```

Образец ответа:

```
{
    "id": 9,
    "author": "Пользователь",
    "text": "Привет МИР!",
    "pub_date": "2022-03-24T06:59:11.493860Z",
    "image": null,
    "group": null
}
```

Пример запроса сообщения в " api/v1/posts/{post_id}/comments/`, чтобы добавить комментарий к сообщению:

```
{
    "post": 9,
    "text": "ЭТО НОВЫЙ МИР?"
}
```

Образец ответа:

```
{
    "id": 1,
    "author": "Пользователь",
    "text": "ЭТО НОВЫЙ МИР?",
    "created": "2022-03-24T07:01:37.926285Z",
    "post": 9
}
```
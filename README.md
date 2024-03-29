# API_Yatube

REST API для социальной сети блогеров Yatube.

## Описание

Проект социальной сети Yatube в рамках обучения на Яндекс Практикум. Благодаря этому проекту можно создавать посты, после прохождения регистрации и аутентификации по токену. Посты можно прикреплять к определенной группе. Можно оставлять комментарии под постами и подписываться на понравившихся авторов. 

## Характеристики

Аутентификация по JWT-токену

Работает со всеми модулями социальной сети Yatube: постами, комментариями, группами, подписчиками.

Получение полного списка всех сообщений на Yatube

Получение списка сообщений, принадлежащих определенной группе

Получение полного списка комментариев ко всем постам

Получение списка комментариев к конкретному посту

Возможность подписки и отписки от автора

Поддерживает методы GET, POST, PUT, PATCH, DELETE

Предоставляет данные в формате JSON


## Стек технологий

- Django REST Framework v.3.12.4- написание проекта на Python v.3.7+
- Simple JWT(djangorestframework-simplejwt v.4.7.2) - работа с JWT-токеном
- Git v.2.35.1 - управление версиями

## Подготовка ПО

### Инструкция для Windows

Установите программное обеспечение: скачайте установочные файлы и запустите их.

Python: https://python.org/downloads/

Visual Studio Code: https://visualstudio.com/download/

Git: https://git-scm.com/download/win/

### Инструкция для Linux (Ubuntu)

Запустите программу Терминал.

1) Сперва установите Python, для этого в терминале выполните команду. Перед установкой терминал попросит вас ввести пароль администратора — сделайте это.
```
sudo apt-get install python3.7 
```
2) По такой же схеме установите Git
```
sudo apt-get install git 
```
3)Чтобы установить редактор вам понадобится менеджер пакетов `snap`. Установите его командой
```
sudo apt install snap 
```
4) Устанавливаем редактор Visual Studio Code из дополнительного набора пакетов:
```
sudo snap install code --classic 
```
5) После того, как всё скачается и установится, вы сможете запустить Visual Studio Code командой `code` в терминале.

## Запуск проекта

1) После установки ПО откройте VSCode и откройте терминал (Терминал - Создать терминал). Внизу спаправа нажмите `+` и выберите Git Bash (если предпочитаете пользоваться стандартной командной строкой powershell, то используйте их).

2) В командной строке войдите в директорию, где планируете развернуть проект. Например:
```
cd /c/Dev/
```
3) Необходимо склонировать репозитарий проекта:
```
git clone https://github.com/Ampolirosinvest/api_final_yatube.git
```
Теперь ваш проект будет храниться в дериктории например: `/c/Dev/api_final_yatube`
Все дальнейшние операции проводятся в дериктории вашего проекта.

4) Установить и активировать виртуальное окружение:
```
python -m venv venv
sourse venv/Scripts/activate
```
5) Установить необходимые зависимости:
```
pip install -r requirements.txt
```
6) Выполните миграции(нужно перейти в директорию, где лежит файл manage.py, например - `/c/Dev/api_final_yatube/yatube_api`):
```
python manage.py makemigrations
python manage.py migrate
```
7) Создайте суперпользователя:
```
python manage.py createsuperuser
```

8) Запустите сервер:
```
python manage.py runserver
```
Ваш проект запустился на `http://127.0.0.1:8000/`

С помощью команды *pytest* вы можете запустить тесты и проверить работу модулей

C помощью *flake8* вы можете проверить оформление кода

9) Можно создать пользователя после запуска проекта:
```
http://127.0.0.1:8000/api/v1/users/
```
отправить POST-запрос:

    {
        "username": "XXXXX",
        "password": "XXXXX"
    }

## Аутентификация

Выполните POST-запрос *localhost:8000/api/v1/jwt/create/* передав поля username и password(см. пункт 9).

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

Пример запроса сообщения в `api/v1/posts/{post_id}/comments/`, чтобы добавить комментарий к сообщению:

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
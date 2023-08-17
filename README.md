# Тестовое задание от Qortex
ЗАДАНИЕ:

Соберите с помощью Django Rest Framework каталог исполнителей и их альбомов с песнями такой структуры:

* Исполнитель
  * Название
* Альбом
  * Исполнитель
  * Год выпуска
* Песня
  * Название
  * Порядковый номер в альбоме

Одна и та же песня может быть включена в несколько альбомов, но под разными порядковыми номерами.

В качестве площадки для демонстрации АПИ подключите к нему Swagger, чтобы можно было проверить работу АПИ через Postman

Результат присылайте в виде репозитория в GitHub с инструкцией по запуску. Бонусом будет, если проект будет запускаться через docker compose.
# Разворачивание
1. [Установить](https://docs.docker.com/compose/install/) Docker
2. [Установить](https://git-scm.com/downloads) Git
3. Клонировать репозиторий:
```no-highlight
git clone https://github.com/tarasenkoartemiy/qortex-test-task.git
```
4. В корневой папке проекта создать файл `.env` и заполнить, используя `template.env`
5. Из корневой папки проекта запустить сервисы:
```no-highlight
docker compose up
```
6. Ознакомиться с доступными endpoints можно тут:
```no-highlight
http://0.0.0.0:8000/schema/swagger/
```
7. Для доступа к административной панели нужно открыть второе окно терминала и в нем создать суперпользователя:
```no-highlight
docker exec -it django python manage.py createsuperuser
```
# Шаги
1. Создать исполнителя
2. Создать ему несколько песен
3. Создать альбом с песнями

# Примеры

1. Создание пользователя:
```no-highlight
{
    "name": "Bob"
}
```
```no-highlight
{
    "id": 1,
    "name": "Bob"
}
```
2. Создание песни:
```no-highlight
{
    "name":"Like a Rolling Stone",
    "executor":1
}
```
```no-highlight
{
    "id": 1,
    "presence": [],
    "name": "Like a Rolling Stone",
    "executor": 1
}
```
Пустой список говорит о том, что эта песня не находится ни в одном альбоме. 
3. Создание еще одной песни:
```no-highlight
{
    "name":"Натали",
    "executor":1
}
```
```no-highlight
{
    "id": 2,
    "presence": [],
    "name": "Натали",
    "executor": 1
}
```
4. Создание альбома:
```no-highlight
{
    "albumtracks": [
        {
            "track":1,
            "serial_number":10
        },
        {
            "track":2,
            "serial_number":42
        }
    ],
    "release_year":2025,
    "executor":1
}
```
```no-highlight
{
    "id": 1,
    "albumtracks": [
        {
            "track": 1,
            "serial_number": 10
        },
        {
            "track": 2,
            "serial_number": 42
        }
    ],
    "release_year": 2025,
    "executor": 1
}
```
5. Просмотр песни, добавленной в альбом:
```no-highlight
{
    "id": 1,
    "presence": [
        {
            "album": 1,
            "serial_number": 10
        }
    ],
    "name": "Like a Rolling Stone",
    "executor": 1
}
```
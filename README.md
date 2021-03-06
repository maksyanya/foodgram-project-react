![Foodgram workflow](https://github.com/maksyanya/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg?branch=master&event=push)

# Foodgram

## Cервис для публикаций и обмена рецептами 

## Доступен по адресу: https://enjoymeal.ru/

### Описание 
#### Cайт Foodgram - онлайн-сервис, на котором пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд. 

### Технологии
Python 3.9.7, Django 3.2.7, Django REST Framework 3.12, PostgresQL, Docker, Yandex.Cloud.

### Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/maksyanya/foodgram-project-react
```

```
cd foodgram-project-react
```

В приложении настроено Continuous Integration и Continuous Deployment:

автоматический запуск тестов,
обновление образов на Docker Hub,
автоматический деплой на боевой сервер при пуше в главную ветку main.

### Описание API

Для ознакомления с API следует открыть ReDoc.

Для этого необходимо запустить контейнер /frontend/:

```
docker-compose up
```

В окне браузера необходимо откройть страницу по адресу:

```
http://localhost/redoc/
```


#### Запуск приложения в контейнерах

- В директории infra/ создайте файл .env, в котором опишите переменные: '''DB_ENGINE=django.db.backends.postgresql''' '''DB_NAME= # название БД\ POSTGRES_USER= # ваше имя пользователя''' '''POSTGRES_PASSWORD= # пароль для доступа к БД''' '''DB_HOST=db''' '''DB_PORT=5432'''
- из директории infra/ соберите образ командой

```
docker-compose up -d --build
```

#### Создаём .env файла. В файле "env.example" приведён пример шаблона:

DB_ENGINE=django.db.backends.postgresql - указываем, что работаем с postgresql
DB_NAME - указываем имя БД
POSTGRES_USER - необходимо указать логин, который будет использоваться для подключения к БД
POSTGRES_PASSWORD - необходимо указать пароль к логину для подключения к БД
DB_HOST=db - название сервиса (контейнера)
DB_PORT=5432 - порт для подключения к БД

- Выполнить миграции

```
docker-compose exec web python manage.py migrate
```

- Собрать статику

```
docker-compose exec web python manage.py collectstatic --no-input
```

- Зарегистрировать суперюзера

```
docker-compose exec web python manage.py createsuperuser
```

#### Заполнение базы данных из файлов *.json

Проект имеет возможность с помощью специального скрипта наполнить БД ингредиентами из файла *.json
Данный способ хорош тем, что большая база ингредиентов будет уже подготовлена для создания рецептов.

Для заполнения БД ингредиентами необходимо выполнить следующие команды:

```
docker-compose exec backend bash
```
```
python manage.py shell < autofill.py
```

Сообщение 'Ингредиенты загружены в базу! Данные из *.json теперь в базе.'

Файл со скриптом находится в директории ./backend/

# Yatube API

Учебный проект, реализующий backend и api платформы для блогов. 


# Краткое описание


## Посты и комментарии

Через api можно получать, создавать, менять и удалять посты и комментарии. Доступ на чтение открыт без авторизации, доступ на изменение контента открыт только аутентифицированным авторам контента. **Посты поддерживают добавление картинок.**

## Группы

Доступны для чтения. Пост можно прикрепит к группе (для этого надо выяснить id группы)

## Подписки

Есть лента подписок с поиском по автору. **Пользователь может только добавлять себе подписки, но не может редактировать или удалять их.**


# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AleksandraMikh/api_final_yatube.git

```

```
cd yatube_api

```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env

```

```
source env/bin/activate

```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip

```

```
pip install -r requirements.txt

```

Выполнить миграции:

```
python3 manage.py migrate

```

Запустить проект:

```
python3 manage.py runserver
```

# Документация к api:

Полный список эндпойнтов, примеров запросов и возможных ответов <code>[в документации](<https://github.com/AleksandraMikh/api_final_yatube/blob/79b4f6e75aa1aa5d0af25a96fba5cbf508165889/redoc.yaml>)
</code>

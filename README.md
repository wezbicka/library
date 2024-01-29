# library

 Тестовое задание для 1AK.BY
Проект выполнен в рамках технического задания. Описание [здесь](https://github.com/wezbicka/library/blob/main/Test_task)

## Требования

У Вас уже должен бать установлен python версии 3.10 и выше

## Чтобы развернуть проект локально:
### Клонируйте данный репозиторий и перейдите с директорию с проектом. Можете и zipом скачать

```
    git clone https://github.com/wezbicka/library.git
    cd library
 ```

### Создайте и активируйте виртуальное окружение

```
    python -m venv venv
    source ./venv/Scripts/activate  #для Windows
    source ./venv/bin/activate      #для Linux и macOS
```

### Создайте файл `.env` для чувствительных данных

Заполните его как здесь. Вообще его нельзя никому сообщать
```
SECRET_KEY='django-insecure-&v%4qvl*^djvm&-f-@h+$j^14e2sy(eh3sg-ix+j-!quf3rx-s'
ALLOWED_HOSTS = '127.0.0.1','localhost'
```

### Установите требуемые зависимости

Выполните команду в терминале Bush
```
pip install -r requirements.txt
```

### Запустите проект

```
python manage.py runserver
```

### Миграции
Если используете мою БД, то переходите к следующему шагу

Если хотите создать новую БД, то удалить файл `db.sqlite3` из репозитория и проведите миграции командой:

```
python manage.py migrate
```

Будет создана новая БД с необходимыми таблицами и полями.
Затем можете добавить книги через админку

#### Приложение будет доступно по адресу: http://127.0.0.1:8000/

Подробнее об эндпойнтах:
- admin/ - UI. Реализовано добавление книг, записях о выдаче и возврате книг и пользователей через админку

- [127.0.0.1:8000/](http://127.0.0.1:8000/) - вход пользователей

- [signup/](http://127.0.0.1:8000/signup/) - регистрация пользователей

- [reader_account/](http://127.0.0.1:8000/reader_account/) - просмотр взятых пользователем книг

- [return_book/](http://127.0.0.1:8000/return_book/) - форма для возврата книг по коду. Я бы могла реализовать по-другому(не через код книги), но следовала заданию

- [take_book/](http://127.0.0.1:8000/take_book/) - выдача книги

- [books/](http://127.0.0.1:8000/books/) - список доступных на данный момент книг

#### Зайти в админку http://127.0.0.1:8000/admin/  (login: test, password: test)


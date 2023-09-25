# library
 Тестовое задание для 1AK.BY
Проект выполнен в рамках технического задания. Описание [здесь](https://github.com/wezbicka/library/blob/main/Test_task)

## Чтобы развернуть проект локально:
### Клонируйте данный репозиторий и перейдите с директорию с ппроектом
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
### Установите требуемые зависимости
```
pip install -r requirements.txt
```
### Запустите проект
```
python manage.py runserver
```
#### Приложение будет доступно по адресу: http://127.0.0.1:8000/


#### Зайти в админку http://127.0.0.1:8000/admin/  (login: test, password: test)

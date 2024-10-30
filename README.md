## Инструкции для запуска

### Клонировать проект:

```git clone <URL_репозитория>```
    ```cd test```

### Создать виртуальное окружение (рекомендуется):

```python -m venv venv``` # Создание виртуального окружения
```source venv/bin/activate``` # Для Linux/Mac
```venv\Scripts\activate```  # Для Windows

### Установить зависимости:

```pip install -r requirements.txt```

### Применить миграции:

```python manage.py migrate```

### Запустить сервер:

```python manage.py runserver```

### Открыть браузер:

Перейти по адресу http://127.0.0.1:8000/

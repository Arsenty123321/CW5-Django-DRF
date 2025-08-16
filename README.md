# CW-Django-DRF


## Настройка окружения для запуска на хосте
#### Предварительные требования
- Python 3.11
- PostgreSQL >=14


- Выполнить команды:
```
# Подготовка окружения
pip install poetry
poetry install --no-root

# Настройка БД PostgreSQL:
# Создать пользователя для работы с БД
sudo -u postgres psql -c "
CREATE USER [имя_пользователя] WITH ENCRYPTED PASSWORD '[пароль]';
"

# Создать БД с имением magazine
sudo -u postgres psql -c "CREATE DATABASE mailer;"

# Настроить доступ к БД для пользователя
sudo -u postgres psql -c "
ALTER DATABASE mailer OWNER TO [имя_пользователя];
GRANT ALL PRIVILEGES ON DATABASE mailer TO [имя_пользователя];
"
```
- Создать файл .env на основе .env.sample и заполнить значения переменных
- Запустить миграции для подготовки проекта:
```
# Запуск миграций
poetry run ./manage.py migrate
```

- Создать пользователя для администрирования через WEB-UI:
```
# Создание администратора через кастомную команду
# логин и пароль задается в .env файле

poetry run ./manage.py csu

```

### Запуск проекта
```
# Запуск сервера
poetry run ./manage.py runserver
```

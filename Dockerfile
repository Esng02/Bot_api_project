FROM python:3.11

# Установка рабочей директории
WORKDIR /app

# Установка зависимостей
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода
COPY app /app

# Установка и запуск nginx
RUN apt-get update && apt-get install -y nginx && apt-get clean

# Копирование конфигурации nginx
COPY nginx/default.conf /etc/nginx/sites-available/default

# Установка Redis
RUN apt-get install -y redis-server

# Запуск сервисов
CMD service redis-server start && \
    uvicorn main:app --host 0.0.0.0 --port 8000 & \
    python bot.py

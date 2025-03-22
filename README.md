# RSPT API Service

API сервис для веб-приложения РСП-Т.

## Установка

1. Создайте виртуальное окружение:
\\\ash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
\\\

2. Установите зависимости:
\\\ash
pip install -r requirements.txt
\\\

## Запуск

\\\ash
uvicorn api.api:app --reload
\\\

## API Endpoints

- GET / - Приветственное сообщение
- GET /health - Проверка работоспособности сервиса

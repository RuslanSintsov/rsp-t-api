import sys
import os

# Добавляем путь к приложению
path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.append(path)

# Загружаем переменные окружения
from dotenv import load_dotenv
load_dotenv(os.path.join(path, '.env'))

# Импортируем приложение
from main import app

# Создаем WSGI приложение
application = app 
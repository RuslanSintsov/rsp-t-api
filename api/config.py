# Список разрешенных email-адресов для регистрации
ALLOWED_EMAILS = [
    'sintsovro@rsp-m.ru',
    'maeestro@list.ru',
    'izmailovar@rsp-m.ru',
    'velikni@rsp-m.ru',
    'rezanovva@rsp-m.ru',
    'velikmn@rsp-m.ru',
    'gushchinala@rsp-m.ru',
    'velikni-rsp13@mail.ru',
    'sincovakn@rsp-m.ru',
    'zhalmagambetovzhs@rsp-m.ru',
    'lobachevavv@rsp-m.ru',
    'anohinaem@rsp-m.ru',
    'klimovav@rsp-m.ru',
    'mironovnp@rsp-m.ru'
]

# Настройки JWT
JWT_SECRET = 'your-secret-key'  # В продакшене использовать безопасный ключ
JWT_ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Сообщение об ошибке при неразрешенном email
EMAIL_NOT_ALLOWED_MESSAGE = 'Запрет регистрации, адрес E-mail нет в списках разрешенных. Обратитесь к разработчику.'

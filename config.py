import os

# Если True, то будет выводить результат в консоль
DEBUG = os.environ.get('DEBUG', True)

# Строка символов для создания комбинаций стартовых слов
COMBINATIONS_STRING = os.environ.get(
    'COMBINATIONS_STRING', 
    'абвгдеёжзиклмнопрстуфхцчшщъыьэюя')

# Минимальная длина генерируемого стартового слова
MIN_LENGTH_R = os.environ.get('MIN_LENGTH_R', 1)

# Максимальная длина генерируемого стартового слова
MAX_LENGTH_R = os.environ.get('MAX_LENGTH_R', 3)

# Шаблон адреса запроса для получения подсказок из интернет магазина allo.ua
URL_TEMPLATE = os.environ.get(
    'URL_TEMPLATE', 
    'https://allo.ua/catalogsearch/ajax/suggest/?q={}&currentTheme=main')

# Количество потоков работы скрапера
THREAD_COUNT = os.environ.get('THREAD_COUNT', 10)

DB_STRING = os.environ.get(
    'DB_STRING', 
    'sqlite:///suggests.sqlite3')

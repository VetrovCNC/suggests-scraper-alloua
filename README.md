# Suggests Scraper from allo.ua
Сборщик подсказок из поисковой строки интернет-магазина allo.ua (http://allo.ua/)

### Тестовое задание

В повседневной работе вам придется разрабатывать новый сложный функционал, сталкиваться с нестандартными, “открытыми” задачами.
Это тестовое задание нужно для того, чтобы мы смогли увидеть ваш подход к решению задач и общий стиль написания кода.

#### Задача:
С помощью Python 3 нужно собрать подсказки из поисковой строки интернет-магазина allo.ua (http://allo.ua/).

#### Требования:
1. В качестве стартовых слов использовать все возможные комбинации из 1, 2 и 3-х букв;
2. Нужно использовать многопоточность (или асинхронность);
3. Результаты сохранять в локальную базу sqlite;
4. При перезапуске, скрипт должен иметь возможность продолжать исполнение с места, где закончил в прошлый раз;
5. Использовать библиотеку Scrapy нельзя.

#### Критерии:
1. Скорость работы кода;
2. Стабильность работы кода;
3. Оптимальное использование сторонних библиотек;

#### Дедлайн: 3 дня.

### Инструкция по запуску

Создаем новое виртуальное окружение и активируем его

1. `$ python3 -m venv .venv`
2. `$ . ./.venv/bin/activate`

Устанавливаем зависимости:

3. `$ pip install -r requirements.txt`

Запускаем скрипт для проверки работы:

4. `$ python scraper.py`

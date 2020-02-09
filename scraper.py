import json
import requests
from multiprocessing import Pool

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import desc

from models import session, Suggests

import config
from combinations import combinations


def get_suggest_from_site(q):
    url = config.URL_TEMPLATE.format(q)
    r = requests.get(url).json()
    # Проверяем сайт вернул словарь, тогда получаем необходимую информацию по ключу 'query'
    if isinstance(r, dict):
        return r.get('query', '')
    # Иначе возвращаем, то что вернул сайт как есть
    return r


def get_suggest(num_query):
    number, query = num_query
    suggests = get_suggest_from_site(query)
    # Сохраняем в базу полученные данные
    suggest = Suggests(
        number=number,
        query=query,
        suggests=json.dumps(suggests)
    )
    session.add(suggest)
    session.commit()
    if config.DEBUG:
        s = "number = {}, query = {}, suggests = {}".format(number, query, suggests)
        print(s)


def main():
    # Пробуем получить из базы последний обработанный запрос
    last_record = session.query(Suggests).order_by(Suggests.number.desc()).first()
    if last_record:
        number = last_record.number
        query = last_record.query
    else:
        number, query = None, None

    # Инициализируем генератор стартовых слов
    generator = combinations(
        config.COMBINATIONS_STRING,
        config.MIN_LENGTH_R,
        config.MAX_LENGTH_R,
        number=number,
        query=query
    )

    with Pool(config.THREAD_COUNT) as p:
        p.map(get_suggest, generator)


if __name__ == '__main__':
    main()

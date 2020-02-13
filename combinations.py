def combinations(iterable, r, r_max, number=None, query=None):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # начинаем генерацию со строк с одним символом
    r = r if not query else len(query)
    # нумерация сгенерированных комбинаций необходима для того, чтобы
    # можно было из базы данных получить последнюю комбинацию при многопоточной записи
    number = number if number else 0
    n = len(iterable)
    if r > n:
        return
    # приводим к списку т.к. далее будем изменять номера индексов
    indices = list(range(r))
    if not query:
        # первая комбинация без переданной строки query для продолжения
        number += 1
        yield (number, iterable[:r])
    else:
        # если переданная стартовая строка длиннее, чем генерируемые - выходим
        query_len = len(query)
        if query_len > r:
            return
        for f in range(query_len):
            # формируем начальное состояние индексов исходя из стартовой строки query
            indices[f] = iterable.find(query[f])
    while True:
        for i in range(r-1,-1,-1):
            if indices[i] != i + n - r:
                break
        else:
            if r >= r_max:
                return
            yield from combinations(iterable, r+1, r_max, number)
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        number += 1
        yield (number, ''.join((iterable[i] for i in indices)))

def combinations(iterable, r, r_max, number=None, query=None):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # начинаем генерацию со строк с одним символом
    r = r if not query else len(query)
    number = number if number else 0
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    if not query:
        # первая комбинация без переданной строки query для продолжения
        number += 1
        yield (number, ''.join(tuple(pool[i] for i in indices)))
    else:
        # если переданная стартовая строка длиннее, чем генерируемые - выходим
        if len(query) > r:
            return
        for f in range(len(query)):
            # формируем начальное состояние индексов исходя из стартовой строки query
            indices[f] = iterable.find(query[f])
    while True:
        for i in reversed(list(range(r))):
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
        yield (number, ''.join(tuple((pool[i] for i in indices))))

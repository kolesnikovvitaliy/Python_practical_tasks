from collections import namedtuple
import itertools as it

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]


def powerset(items):
    return it.chain.from_iterable(it.combinations(items, r) for r in range(len(items)+1))


def get_weight(combo):
    return sum(x.mass for x in combo)


def get_sum(combo):
    return sum(x.price for x in combo)


n = int(input())
max_combo = max(filter(
    lambda x: get_weight(x) <= n, powerset(items)),
    key=get_sum)

print(*sorted(
    map(lambda x: x.name, max_combo)), sep="\n")\
        if max_combo else print('Рюкзак собрать не удастся')

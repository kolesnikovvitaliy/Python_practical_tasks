from collections import namedtuple
from itertools import groupby

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]


key_sort = lambda x: x.height
persons.sort(key=key_sort)
groups = groupby(persons, key=key_sort)
for height, iter_person in groups:
    print(f'{height}:', ', '.join(sorted(
        map(lambda x: x.name, iter_person))))
    
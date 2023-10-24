from collections import namedtuple
import csv
from datetime import datetime
import sys
_lst = []
with open('meetings.csv', encoding='utf=8') as f:
    file_csv = csv.reader(f, delimiter=',')
    head = next(file_csv)
    Person = namedtuple('Person', head)
    [_lst.append(Person._make(i)) for i in file_csv]

_lst.sort(key=lambda x:
          (datetime.strptime(x.meeting_date, '%d.%m.%Y'),
           datetime.strptime(x.meeting_time, '%H:%M')))

[sys.stdout.writelines(f"{i.surname} {i.name}\n") for i in _lst]
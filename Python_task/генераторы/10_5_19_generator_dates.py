from datetime import date, timedelta
from typing import Generator


def dates(start: date, count: int = None) -> Generator:
    i = start
    while True:
        if count and count == (i-start).days:
            return
        yield i
        try:
            i += timedelta(days=1)
        except OverflowError:
            return

# def dates(start, count=None):
#     count = count or (date.max - start).days + 1
#     for i in range(count):
#         yield start + timedelta(days=i)
from datetime import date
b = {1:[1, 2, 3], 2:[4, 5, 6], 3:[7, 8, 9], 4:[10, 11, 12]}
dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]
for a in dates:
    for key, voluem in b.items():
        if a.month in voluem:
            print(f'{a.year}-Q{key}')




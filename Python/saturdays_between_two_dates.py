from datetime import date

def saturdays_between_two_dates(date1, date2):
    b = 0
    if date1 < date2 or date1 == date2:
        a =  [date.fromordinal(i) for i in range(date1.toordinal(), date2.toordinal()+1)]
        for i in a:
            if i.weekday() == 5:
                b += 1
        return b
    else:
        a =  [date.fromordinal(i) for i in range(date1.toordinal(), date2.toordinal(), -1)]
        for i in a:
            if i.weekday() == 5:
                b += 1
        return b

# date1 = date(2020, 7, 26)
# date2 = date(2020, 7, 2)

# print(saturdays_between_two_dates(date1, date2))
date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))
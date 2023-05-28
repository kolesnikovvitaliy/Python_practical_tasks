from datetime import datetime

def get_in_list(data):
    d = []    
    if type(data) == str:
        d.append(data)
        return d
    return data       

def get_list_dates(data):
    from datetime import timedelta as t
    a = []
    b = []
    for i in get_in_list(data):
        if len(i) < 15:
            a.append(datetime.strptime(i,'%d.%m.%Y'))
        else:
            b.append([datetime.strptime(y,'%d.%m.%Y') for y in [j for j in i.split('-')]])
    for i in range(len(b)):
        a.append(b[i][0])
        while b[i][1] not in a:
            b[i][0] += t(days=1)
            a.append(b[i][0])
    return a    
         
def is_available_date(dates, some_date):
    for i in get_list_dates(some_date):
        if i in get_list_dates(dates):
            return False
    return True

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))



# dates = ['04.11.2021', '05.11.2021-09.11.2021']
# some_date = '01.11.2021-04.11.2021'
# print(is_available_date(dates, some_date))


# dates = ['04.11.2021', '05.11.2021-09.11.2021']
# some_date = '01.11.2021'
# print(is_available_date(dates, some_date))




# dates = ['05.11.2021-09.11.2021']
# some_date = '01.11.2021-04.11.2021'
# print(is_available_date(dates, some_date))
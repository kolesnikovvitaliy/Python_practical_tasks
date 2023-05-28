from datetime import datetime, timedelta

def fill_up_missing_dates(data):
    pattern = '%d.%m.%Y'
    a = [datetime.strptime(i,pattern) for i in data]
    b = [datetime.strptime(str(min(a)), '%Y-%m-%d %H:%M:%S')] 

    while max(b) != max(a):        
        b.append(max(b) + timedelta(days=1))

    return [datetime.strftime(i,pattern) for i in b]
    # for i in b:
    #     c.append(datetime.strftime(i,pattern))
    
    # return c
         
# dates = ['20.07.2020', '16.05.2021', '19.01.2022', '18.11.2021', '17.10.2021', '15.03.2021']
# print(len(fill_up_missing_dates(dates)))
dates = ['20.07.2021', '16.05.2021', '19.01.2021', '16.11.2021', '17.10.2021', '15.03.2021']
print(len(fill_up_missing_dates(dates)))
#304
#549
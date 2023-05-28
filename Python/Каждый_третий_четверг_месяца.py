from datetime import date, timedelta
import calendar

def get_all_tuesday(year):
    lst = set()
    for month in range(1, 13):
        for i in range(len(calendar.monthcalendar(year, month))):
            tuesday = calendar.monthcalendar(year, month)[i][3]
            if tuesday in range(15, 22) and tuesday in calendar.monthcalendar(year, month)[i]:
                lst.add(date(year, month, tuesday))
    
    for i in sorted(lst):
        print(date.strftime(i,'%d.%m.%Y'), sep='\n')    

y = int(input())        
get_all_tuesday(y)




# import calendar, locale

# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

# print(calendar.calendar(2022, m=4).title())
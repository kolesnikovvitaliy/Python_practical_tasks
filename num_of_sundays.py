from datetime import datetime
def num_of_sundays(y):
    return datetime(year=y,month=12,day=31).strftime('%U')
#    datetime.date.today().strftime("%j")



print(num_of_sundays(2021))
from datetime import date
def get_date_range(date1, date2):
    if date1 == date2:
        return [date1]
    elif date1 < date2:
        return [date.fromordinal(i) for i in range(date1.toordinal(), date2.toordinal()+1)]
    return [] 
        

    


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')
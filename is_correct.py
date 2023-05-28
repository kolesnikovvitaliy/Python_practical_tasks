from datetime import date
b = 0
a = []
def is_correct(day, month, year):
    try:
        date(int(year), int(month), int(day))
        return "Корректная"
    except:
        return "Некорректная"
        
while "end" not in a:
        a.append(input())
a.pop()   

for i in a:
    day, month, year = i.split('.')
    print(is_correct(day, month, year))
    if is_correct(day, month, year) == "Корректная":
        b += 1
print(b)
#print(is_correct(31, 13, 2021))
#my_date = date(int(year),int(month),int(day)) 
#day, month, year = date_check.split('.')

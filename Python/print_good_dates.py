from datetime import date
def print_good_dates(dates):
    print(*[i.strftime('%B %d, %Y') for i in sorted(filter(lambda x: (x.day + x.month) == 29, dates))], sep="\n")



dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)
# Sample Output 1:

# September 20, 1992
# October 19, 1992

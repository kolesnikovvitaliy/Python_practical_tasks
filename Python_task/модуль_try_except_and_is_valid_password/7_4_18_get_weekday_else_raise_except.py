import calendar
import locale


locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def chec_digit(num):
    if not isinstance(num, int):
        raise TypeError('Аргумент не является целым числом')
    elif num not in range(1, 8):
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    return num


def get_weekday(number):
    return calendar.day_name[chec_digit(number)-1]
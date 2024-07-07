
"""
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
"""
"""
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""
from datetime import datetime
import sys

__all__ = ['check_year', 'date_validator']

CHECK_NORMAL_1 = 4
CHECK_NORMAL_2 = 100
CHECK_NORMAL_3 = 400
YEARS = range(1, 10000)


def _check_leap_year(date: str) -> bool:
    year = int(date.split(".")[-1])
    if year in YEARS and year % CHECK_NORMAL_1 == 0 and year % CHECK_NORMAL_2 != 0 or year % CHECK_NORMAL_3 == 0:
        return True

    return False


def check_year(year: str) -> bool:
    is_year = True
    try:
        datetime.strptime(year, "%d.%m.%Y").date()
    except ValueError:
        is_year = False

    return is_year


def date_validator(date: str) -> str:
    if check_year(date):
        return 'Високосный' if _check_leap_year(date) else 'Не является високосным'

    return f'Дата заполнена некорректно'


if __name__ == '__main__':
    _, *date = sys.argv
    if date:
        print(date_validator(*date))
    else:
        date = input('Введите дату:')
        print(date_validator(date))
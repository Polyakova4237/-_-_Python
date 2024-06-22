"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
"""

LOWER_LIMIT = 0
UPPER_LIMIT = 10000
ATTEMPTS = 10

from random import randint

num = randint(LOWER_LIMIT, UPPER_LIMIT)
A = int(input(f'попробуйте угадать число: '))
while A != num:
    while ATTEMPTS > 0:
        if A > num:
            print("Меньше ")
        else:
            print("Больше ")
        A = int(input(f'ещё попытка: '))
        ATTEMPTS -=1
    print("у вас закончились попытки")
    break
print("вы угадали!")

"""Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч."""

num = int(input(f'введите число: '))

LOWER_LIMIT = 0
UPPER_LIMIT = 100000
k=0
while num>LOWER_LIMIT or num<UPPER_LIMIT:
    for i in range(2, num//2+1):
        if (num%i==0):

            k=k+1
    if (k <= 0):
        print("Число простое")
        break
    else:
        print("Число не является простым")
        break

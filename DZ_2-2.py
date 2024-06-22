"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions
"""

N = 2
TEXT_INPUT = 'Введите {} строку вида: "a/b": '
ONE_STR = '1'
fractions = []


class Fraction:

    def __init__(self, expression):
        self.numerator, self.denominator = Fraction.split_expression(expression)

    @staticmethod
    def split_expression(expression):
        #Разделяет числитель и знаменатель
        return (int(num) for num in expression.split('/'))

    def __add__(self, other):
        #Считает сумму дробей
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        nod = self.gcd(numerator, denominator)
        return Fraction(f'{numerator // nod}/{denominator // nod}')

    def gcd(self, x, y):
    #Ищет наименьший общий делитель
        if y == 0:
            return x

        return self.gcd(y, x % y)

    def __mul__(self, other):
        """Считает произведение дробей"""
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        nod = self.gcd(numerator, denominator)
        return Fraction(f'{numerator // nod}/{denominator // nod}')

    def __str__(self):
        return f'{self.numerator}/{self.denominator}' if self.numerator != self.denominator else ONE_STR

    def __repr__(self):
        return f'Fracton({self.numerator}, {self.denominator})'


def input_data(i: int) -> str:
    #Вводит данные
    return input(TEXT_INPUT.format(i))


def run():
    for i in range(1, N + 1):
        expression = input_data(i)
        fractions.append(Fraction(expression))


if __name__ == '__main__':
    run()
    print(fractions[0] * fractions[-1])
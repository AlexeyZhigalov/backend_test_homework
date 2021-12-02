<<<<<<< HEAD
from math import sqrt

message = (
            'Добро пожаловать в самую лучшую программу для '
            'вычисления квадратного корня из заданного числа'
)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Формирует результат."""
    if your_number >= 0:
        root = calculate_square_root(your_number)
        print(f'Мы вычислили корень квадратный из введенного вами числа.'
              f' Это будет: {root}')


print(message)
calc(25.5)

=======
from math import *
import itertools


message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'

def  CalculateSquareRoot (Number ):
    """ Вычисляет квадратный корень"""
    return  sqrt(Number )

def calc(your_number) :
    if your_number<=0:
        return    
     
    root = 0
    print(f"Мы вычислили корень квадратный из введенного вами числа. Это будет: {CalculateSquareRoot(your_number)}")


print (message)
calc (25.5)
>>>>>>> 09af60d6ea093a64fb3549ef1b93b6988956a567

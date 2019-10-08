"""

Задача 2. Уровень - да ты математик.

Условие: Подсчет площади и периметра прямоугольника.
Входные данные: стороны %a% и %b% прямоугольника. 
Выходные данные: площадь и периметр данного прямоугольника.


Пример:

Ввод:                                         Вывод:
2 3                                           Perimeter 10
                                              Square 6

4 4                                           Perimeter 16
                                              Square 16


10 15                                         Perimeter 50
                                              Square 150


2 2                                           Perimeter 8
                                              Square 4

"""



a,b=map(float, input().split())
p=2*a+2*b
s=a*b
print('Perimeter',p)
print('Square', s)
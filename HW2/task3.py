# Задача 3. Уровень - шахматный мачо.
# Условие: в шахматах конь ходит буквой Г. В школе BPS есть особый конь на шахматной доске: он тоже ходит буквой Г,
# только по горизонтали он может пройти 2 клетки, а по вертикали 5, или наоборот. Даны две различные клетки шахматной доски.
# Требуется определить,
# возможно ли конем из школы BPS перейти из одной клетки шахматной доски в другую.

# Входные данные : 4 целых числа (все > 0). В первой строке вводится номер столбца 1 клетки. На второй строке - номер
# строки первой клетки. Потом аналогично на третьей и четвертой строках вводится информацию о 2 клетке.

# Выходные данные: "YESSSS!" если такой ход возможен, "No no" - если такой ход невозможен.

# Пример:
# Ввод:                                              # Вывод:
# 1
# 1
# 4
# 3                                                  No no


# 6
# 3
# 1
# 1                                                  YESSSS!

y1=int(input())
x1=int(input())
y2=int(input())
x2=int(input())

if (y1 + x1) < (y2 + x2) and y2 > x2 and y1 + 5 == y2 and x1 + 2 == x2:
       print("YESSSS!")
elif (y1 + x1) < (y2 + x2) and y2 < x2 and y1 + 2 == y2 and x1 + 5 == x2:
    print("YESSSS!")
elif (y1 + x1) > (y2 + x2) and y1 < x1 and y1 - 2 == y2 and x1 - 5 == x2:
    print("YESSSS!")
elif (y1 + x1) > (y2 + x2) and y1 > x1 and y1 - 5 == y2 and x1 - 2 == x2:
    print("YESSSS!")
else:
    print ("No no")


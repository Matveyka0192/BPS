# Задание 2. Уровень - диванный воин.
# Условие: необходимо написать программу, которая считывает с клавиатуры одно за другим два вещестенных числа A и B, 
# и затем строку. Если эта строка является обозначением одной из четырёх 
# основных математических операций (+, -, * или /), то выведите результат применения этой 
# операции к введенным ранее числам, в противном случае выведите «ЫЫЫЫЫЫ». 
# Также «ЫЫЫЫЫЫ» следует вывести, если пользователь захочет поделить на ноль.

# Пример:
# Ввод:                                                              # Вывод:
# 23.5
# 55.2
# ЙЦУКЕН                                                             ЫЫЫЫЫЫ


# 23.5
# 0
# /                                                                  ЫЫЫЫЫЫ


# 20.1
# 10.1
# +                                                                  30.2

a = float(input())
b = float(input())
c = str(input())
if c == '+':
    x = a + b
    print(x)
elif c == '-':
    x = a - b
    print(x)
elif c == '*':
    x = a * b
    print(x)
elif c == '/' and b != 0:
    x = a / b
    print(x)
else:
    print('ЫЫЫЫЫЫ')
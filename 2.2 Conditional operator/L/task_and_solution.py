"""
Музыкальный инструмент
Есть много музыкальных инструментов, но Вася обожает треугольник.

У него завалялось немного алюминиевых трубочек разной длины, и он задаётся вопросом, а можно ли из них сделать любимый музыкальный инструмент.

Формат ввода
Три числа — длины трубочек, каждое с новой строки.

Формат вывода
YES — если Васе удастся создать музыкальный треугольник, иначе — NO

Примечание
Обратите внимание, что в треугольнике любая сторона меньше суммы двух других.

Пример 1
Ввод
3
3
3

Вывод
YES

Пример 2
Ввод
1
2
3

Вывод
NO


Ограничение памяти
64.0 Мб

Ограничение времени
1 с

Ввод
стандартный ввод или input.txt

Вывод
стандартный вывод или output.txt

"""

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 < (n3 + n2) and n2 < (n1 + n3) and n3 < (n2 + n1):
    print('YES')
else:
    print('NO')

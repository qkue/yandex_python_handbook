"""
Доставка
Продуктовый склад и магазин находятся на одной дороге города Н.
Склад находится на отметке A км, а магазин — B км. Средняя скорость автомобиля, доставляющего товары, C км/ч.
За какое время продукты попадают со склада в магазин?

Формат ввода
Три натуральных числа A, B и C, каждое на отдельной строке.

Формат вывода
Одно рациональное число с точностью до сотых.

Пример 1
Ввод
10
32
5

Вывод
4.40

Пример 2
Ввод
1
100
30

Вывод
3.30


Ограничение памяти
64.0 Мб

Ограничение времени
1 с

Ввод
стандартный ввод или input.txt

Вывод
стандартный вывод или output.txt

"""

a = int(input())
b = int(input())
c = int(input())

print(round((b - a) / c, 2))
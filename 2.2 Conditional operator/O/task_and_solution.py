"""
Властелин Чисел: Возвращение Цезаря
До победы над злом остался один шаг — разрушить логово Зерона.

Для этого нужно создать трёхзначное магическое число, которое будет сильнее двух двухзначных защитных чисел Зерона.

Самый простой способ создать сильное число:

первой взять максимальную цифру из всех защитных чисел;
последней — минимальную;
в середину поставить сумму оставшихся без учёта переноса разряда.
Помогите одолеть зло.

Формат ввода
В двух строках записаны защитные числа Зерона.

Формат вывода
Одно трёхзначное число, которое приведёт к победе.

Пример 1
Ввод
31
11

Вывод
321

Пример 2
Ввод
49
17

Вывод
911


Ограничение памяти
64.0 Мб

Ограничение времени
1 с

Ввод
стандартный ввод или input.txt

Вывод
стандартный вывод или output.txt

"""

num1 = str(input())
num2 = str(input())
num1_num2 = num1 + num2
num3 = ''


numsort = sorted(num1_num2)
num3 += numsort[-1]
numavg = (int(numsort[1]) + int(numsort[2])) % 10
num3 += str(numavg)
num3 += numsort[0]

print(num3)

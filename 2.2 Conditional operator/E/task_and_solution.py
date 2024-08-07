"""
Яблоки
У Пети было 7 яблок, а у Васи 6.

Затем Петя отдал 3 яблока Васе, а у Толи взял 2 яблока.

Вася попросил у Толи 5 яблок, но он отдал Гене 2.

Затем Дима дал Пете N яблок, а Васе M.

Так у кого в итоге яблок больше — у Пети или Васи?

Формат ввода
В первой строке записано натуральное число N.
Во второй — M.

Формат вывода
Имя ребёнка, у которого больше яблок.

Пример 1
Ввод
3
5

Вывод
Вася

Пример 2
Ввод
10
2

Вывод
Петя


Ограничение памяти
64.0 Мб

Ограничение времени
1 с

Ввод
стандартный ввод или input.txt

Вывод
стандартный вывод или output.txt

"""

n = int(input())
m = int(input())

p = 7 - 3 + 2 + n
v = 6 + 3 + 5 - 2 + m

if p > v:
    print('Петя')
else:
    print('Вася')

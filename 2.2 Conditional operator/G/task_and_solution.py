"""
А роза упала на лапу Азора
Существуют такое интересное понятие как палиндром — число, слово, предложение и так далее, которое и слева-направо, и справа-налево читается одинаково.

Напишите программу, которая проверяет, является ли число палиндромом.

Формат ввода
Одно четырёхзначное число

Формат вывода
YES если число является палиндромом, иначе — NO.

Пример 1
Ввод
1234

Вывод
NO

Пример 2
Ввод
2332

Вывод
YES


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
reverse = str(n)[::-1]

if n == int(reverse):
    print('YES')
else:
    print('NO')
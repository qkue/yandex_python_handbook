"""
Делу — время, потехе — час
Давайте передохнём от автоматизации и сделаем что-то действительно интересное.

Формат ввода
Одно натуральное число N

Формат вывода
N строк с фразой: "Купи слона!"

Пример 1
Ввод
1

Вывод
Купи слона!

Пример 2
Ввод
3

Вывод
Купи слона!
Купи слона!
Купи слона!


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
print(str(n * ('Купи слона!' + '\n')))
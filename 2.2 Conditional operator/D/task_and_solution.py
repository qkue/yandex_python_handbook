"""
Список победителей
Длина трассы — 43872м, и зрители хотят узнать имя победителя.

Нам известны средние скорости трёх фаворитов – Пети, Васи и Толи. Помогите подвести итоги гонки.

Формат ввода
В первой строке записана средняя скорость Пети.
Во второй — Васи.
В третьей — Толи.

Формат вывода
Имена победителей в порядке занятых мест.

Пример 1
Ввод
10
5
7

Вывод
1. Петя
2. Толя
3. Вася

Пример 2
Ввод
5
7
10

Вывод
1. Толя
2. Вася
3. Петя


Ограничение памяти
64.0 Мб

Ограничение времени
1 с

Ввод
стандартный ввод или input.txt

Вывод
стандартный вывод или output.txt

"""

p = int(input())
v = int(input())
t = int(input())

if p > v and p > t:
    if v > t:
        print(f'1. Петя')
        print(f'2. Вася')
        print(f'3. Толя')
    else:
        print(f'1. Петя')
        print(f'2. Толя')
        print(f'3. Вася') 

elif v > p and v > t:
    if p > t:
        print(f'1. Вася')
        print(f'2. Петя')
        print(f'3. Толя')  
    else:
        print(f'1. Вася')
        print(f'2. Толя')
        print(f'3. Петя')

else:
    if p > v:
        print(f'1. Толя')
        print(f'2. Петя')
        print(f'3. Вася')                                
    else:
        print(f'1. Толя')
        print(f'2. Вася')
        print(f'3. Петя')        

"""
Зайка — 2
По пути домой родители вновь решили сыграть с детьми в поиск зверушек.

Формат ввода
Три строки описывающих придорожную местность.

Формат вывода
Строка в которой есть зайка, а затем её длина.
Если таких строк несколько, выбрать ту, что меньше всех лексикографически.

Пример 1
Ввод
березка елочка зайка волк березка
сосна сосна сосна елочка грибочки медведь
сосна сосна сосна белочка сосна белочка

Вывод
березка елочка зайка волк березка 33

Пример 2
Ввод
зайка березка
березка зайка
березка елочка березка

Вывод
березка зайка 13


Ограничение памяти
64.0 Мб

Ограничение времени
1 с

Ввод
стандартный ввод или input.txt

Вывод
стандартный вывод или output.txt

"""

str1 = str(input())
str2 = str(input())
str3 = str(input())
rab = 'зайка'

if rab in str1 and rab in str2 and rab in str3:
    print(f'{min(str1, str2, str3)} {len(min(str1, str2, str3))}')
elif rab in str1 and rab in str2:
    print(f'{min(str1, str2)} {len(min(str1, str2))}')
elif rab in str2 and rab in str3:
    print(f'{min(str3, str2)} {len(min(str3, str2))}')
elif rab in str1 and rab in str3:
    print(f'{min(str1, str3)} {len(min(str1, str3))}')
elif rab in str1:
    print(f'{str1} {len(str1)}')
elif rab in str2:
    print(f'{str2} {len(str2)}')
elif rab in str3:
    print(f'{str3} {len(str3)}')

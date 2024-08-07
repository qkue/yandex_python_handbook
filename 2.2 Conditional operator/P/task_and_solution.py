"""
Легенды велогонок возвращаются: кто быстрее?
В новом сезоне за первенство в велогонках вновь борются лучшие из лучших. Протяжённость заключительной трассы — 43872м, и все хотят знать, кто получит золотую медаль.

Нам известны средние скорости трёх претендентов на победу – Пети, Васи и Толи. Кто из них победит?

Формат ввода
В первой строке записана средняя скорость Пети.
Во второй — Васи.
В третьей — Толи.

Формат вывода
Красивый пьедестал (ширина ступеней 8 символов).

Примечание
В данный момент визуализация тестов работает некорректно.
Ответ на первый тест:

          Петя          
  Толя  
                  Вася  
   II      I      III   
   
Пример 1
Ввод
10
5
7

Вывод
          Петя          
  Толя  
                  Вася  
   II      I      III 
   
Пример 2
Ввод
5
7
10

Вывод
          Толя          
  Вася  
                  Петя  
   II      I      III   


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
        f = 'Петя'
        s = 'Вася'
        t = 'Толя'
    else:
        f = 'Петя'
        s = 'Толя'
        t = 'Вася'

elif v > p and v > t:
    if p > t:
        f = 'Вася'
        s = 'Петя'
        t = 'Толя'
    else:
        f = 'Вася'
        s = 'Толя'
        t = 'Петя'

else:
    if p > v:
        f = 'Толя'
        s = 'Петя'
        t = 'Вася'
    else:
        f = 'Толя'
        s = 'Вася'
        t = 'Петя'

print('{:^8}'.format(''), end='')
print('{:^8}'.format(f))
print('{:^8}'.format(s))
print('{:^16}'.format(''), end='')
print('{:^8}'.format(t))
print('{:^8}'.format('II'), end='')
print('{:^8}'.format('I'), end='')
print('{:^8}'.format('III'), end='')


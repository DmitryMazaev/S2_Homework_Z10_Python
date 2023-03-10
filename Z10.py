# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random

n = int(input("Введите количество монет на столе: "))
obverse = 0
reverse = 0
for i in range(n):
    a = random.randint(0,1) # 0 - орел, 1 - решка
    print(a, end = " ")
    if a == 0:
        obverse += 1
    else:
        reverse += 1
if obverse < reverse:
    print(f'Минимальное число монет, которые нужно перевернуть, лежит вверх орлом и составляет {obverse}')
elif obverse > reverse:
    print(f'Минимальное число монет, которые нужно перевернуть, лежит вверх решкой и составляет {reverse}')
else:
    print(f'Количество монет, лежащих орлом и решкой, равно и составляет {reverse}')
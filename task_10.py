# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество
# монет, которые нужно перевернуть

from random import randint

n = int(input('Введите количество монеток на столе: '))
coins = []
for i in range(n):
    coins.append(randint(0, 1))
print(coins)

tails = 0
heads = 0

for i in range(n):
    if coins[i] == 1:
        tails += 1
    else:
        heads += 1
if tails < heads:
    print(
        f'Переверните {tails} монет с решки на орла')
elif tails > heads:
    print(
        f'Переверните {heads} монет с орла на решку')
else:
    print(
        f'Количество орлов и решек одинаково, по {tails}')

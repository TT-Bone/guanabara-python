tupla = ('Panquecas', 5.50, 'Waffles', 4.30, 'Ovos e Bacon', 6.30, 'Linguiça e BatataRosti', 7.40, 'Omelete', 4.40, 'Cheese Burger', 8.80)

for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<45}', end = '')
    elif pos % 2 == 1:
        print(f'R$ {tupla[pos]:>4.2f}')

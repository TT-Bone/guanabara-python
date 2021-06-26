print('=-' * 10, 'TABUADA', '=-' * 10)
qtdade = 0

while True:
    num = int(input('De qual número você quer saber a tabuada? '))
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{cont} x {num} = {cont * num}')
    print('-' * 15)
    qtdade += 1

print(f'Fim! Você fez a tabuada de {qtdade} números.')


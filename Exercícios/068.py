from random import randint
print('><' * 10, 'O JOGO DO PAR OU ÍMPAR', '><' * 10)
cont = 0

while True:
    print('-' * 30)
    num = int(input('Escolha um número: '))
    escolha = str(input('Você escolha PAR ou ÍMPAR [P/I]? ')).strip().upper()[0]
    pc = randint(1, 10)
    soma = num + pc
    if soma % 2 == 0 and escolha == 'P':
        print(f'Seu número {num} e do PC {pc} => {num} + {pc} = {soma}')
        print(f'{soma} é PAR e você GANHOU!')
        cont += 1
    if soma % 2 != 0 and escolha == 'I':
        print(f'Seu número {num} e do PC {pc} => {num} + {pc} = {soma}')
        print(f'{soma} é IMPAR e você GANHOU!')
        cont += 1
    if soma % 2 == 0 and escolha == 'I':
        print(f'Seu número {num} e do PC {pc} => {num} + {pc} = {soma}')
        print(f'{soma} é PAR e você PERDEU!')
        break
    if soma % 2 != 0 and escolha == 'P':
        print(f'Seu número {num} e do PC {pc} => {num} + {pc} = {soma}')
        print(f'{soma} é ÍMAPAR e você PERDEU!')
        break
print('-' * 30)
print(f'Você ganhou {cont}x do computador!')

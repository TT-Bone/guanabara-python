'''
Desenvolva um programa que leia 4 valores por um teclado, e guarde-os em uma tupla. No final, mostre:
1. Quantas vezes apareceu o valor 9.
2. Em que posição foi digitado o primeiro valor 3.
3. Quais foram os números pares.
'''
tupla = (int(input('Número 1: ')), 
        int(input('Número 1: ')),
        int(input('Número 1: ')),
        int(input('Número 1: ')))

if 9 in tupla:
    print(f'''1. O valor 9 apareceu {tupla.count(9)}x;''')
else:
    print(f'1. O valor 9 não apareceu nessa lista.')

if 3 in tupla:
    print(f'2. A primeira posição de 3 foi na {tupla.index(3) + 1};')
else:
    print('2. Não houve digitação do número 3 desta vez.')

print('3. Os números pares dessa seleção foram: ', end = '')
for cont in range(0, len(tupla)):
    if tupla[cont] % 2 == 0:
        print(tupla[cont], end = ' ')

print('''.
Fim.''')

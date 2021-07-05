'''
Crie um programa que crie uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

txt1 = str(input('Texto 1: ')).strip()
txt2 = str(input('Texto 2: ')).strip()
txt3 = str(input('Texto 3: ')).strip()

tupla = (txt1, txt2, txt3)
vogais = ('a', 'e', 'i', 'o', 'u')

for txt in tupla:
    print(f'Para {txt}:', end='')
    for vogal in vogais:
        if txt.count(vogal) > 0:
            print(f' {vogal}', end = ' ')
    print('\n')    
    
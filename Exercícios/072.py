'''
Crie um programa que tenha uma tupla, totalmente preenchida com uma contagem com por extenso, de zero até vinte.
Seu programa deverá lerum número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    while True:
        escolha = int(input('Digite um número de 0 a 20: '))
        if 0 <= escolha <= 20:
            break
        else:
            print('Valor inválido. Tente novamente.')
    dec = str(input('Deseja Continuar: [S/N] ')).strip().upper()[0]
    
print(f'Você escolheu o número {num[escolha]}.')

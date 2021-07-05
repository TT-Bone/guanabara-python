'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
# Armazenando os valores
num = []
for cont in range(0,5):
    num.append(int(input(f'Valor {cont + 1}: ')))

# Definindo limites (maior e menor número), o que no final das contas não serviu para nada. Tudo poderia ser feito usando os comandos diretos.
maior = max(num)
menor = min(num)

print(f'Os valores digitados foram: {num}')

# Achando a localização do maior valor:
print(f'O maior valor foi {max(num)}, e suas posições: ', end = '')
for loc, val in enumerate(num):
    if val == max(num):
        print(f'{loc + 1}', end = ' ')
print()

# Achando a localização do menor valor:
print(f'O menor valor foi {min(num)}, e suas posições: ', end = '')
for loc, val in enumerate(num):
    if val == min(num):
        print(f'{loc + 1}', end = ' ')
print()

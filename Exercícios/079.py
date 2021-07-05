'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
'''

lista = []
voltas = 0

while True:
    temp = int(input('Digite seu valor: '))
    if temp in lista:
        print(f'O valor {temp} já foi adicionado.')
    else:
        print('Este valor ainda não foi adicionado. Vou colocá-lo agora mesmo.')
        lista.append(temp)
    
    flag = str(input('Deseja digitar mais algum valor? [S/N]  ')).strip().upper()[0]
    if flag == 'N':
        break
    if flag == 'S':
        voltas += 1
    else:
        print('Comando Inválido. Tente novamente: ')
        
lista.sort()

print(lista)
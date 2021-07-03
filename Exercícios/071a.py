'''
//Crie um programa que leia o nome e o preço de várias produtos. O programam deverá perguntar se o usuário vai continuar. No final, mostre:
1. Qual é o total gasto na compra.
2. Quantos produtos custam mais de R$1000
3. Qual é o nome do produto mais barato.

// Fiquei bem satisfeito por ter conseguido pensar nessa possibilidade sozinho, depois de precisar de algum tempo pensando em como conseguiria. Quase desisti, para ser sincero. Porém diferente da sugestão de resolução do Guanabara, eu "movimento o dinheiro" para ser descontado a medida que o programa avança. Ele vai perdendo dinheiro a cada novo WHILE.
'''

print('Programa Caixa Eletrônico')

valor = int(input('Qual valor pretende tirar? R$'))
valorinicial = valor
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0
voltas = 0

while True:
    voltas += 1
    while valor > 50:
        valor -= 50
        nota50 += 1
    
    while valor > 20:
        valor -= 20
        nota20 += 1

    while valor > 10:
        valor -= 10
        nota10 += 1

    while valor != 0:
        valor -= 1
        nota1 += 1
    if valor == 0:
        break

print(f'''Seu pedido foi de R${valorinicial},00. 
Foram retiradas {nota50} notas de R$50,00;
Foram retiradas {nota20} notas de R$20,00;
Foram retiradas {nota10} notas de R$10,00;
E foram retiradas {nota1} notas de R$1,00.''')
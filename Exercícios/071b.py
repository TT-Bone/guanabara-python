'''
//Crie um programa que leia o nome e o preço de várias produtos. O programam deverá perguntar se o usuário vai continuar. No final, mostre:
1. Qual é o total gasto na compra.
2. Quantos produtos custam mais de R$1000
3. Qual é o nome do produto mais barato.

//Um programa um pouco mais complexo de se pensar sozinho. Na versão 071a eu criei um raciocínio parecido, porém a ideia é que o valor todo fosse "perdendo" dinheiro a medida que o programa fosse evoluindo. Ao contrário daqui que o dinheiro é "descontado" sempre no mesmo lugar, no IF da linha 18.
O interessante foi ver a forma como ele opera o ELSE da linha 21, colocando o entendimento do perfeito funcionamento, trazendo o PRINT para aquele momento.
'''


valor = int(input('Valor a ser sacado: R$'))
total = valor
ced = 50
numced = 0

while True:
    if valor >= ced:
        valor -= ced
        numced += 1
    else:
        if numced > 0:
            print(f'Retirada de {numced} de R${ced},00.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        numced = 0
        if valor == 0:
            break

print(f'''O total retirado foi R${total},00.
O nosso Banco agradece a preferência.''')

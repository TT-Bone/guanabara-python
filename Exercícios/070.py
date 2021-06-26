voltas = 0
total = 0
caros = 0
valorbarato = 0
maisbarato = ''
flag = ''

while True:
    voltas += 1
    nome = str(input(f'Nome do protudo {voltas}: ')).strip()
    valor = int(input(f'Valor do produto {voltas}: R$'))

    total += valor
    
    if valorbarato == 0:
        valorbarato = valor
    if valor > 1000:
        caros += 1
    if valor < valorbarato:
        valorbarato = valor
        maisbarato = nome
    
    flag = str(input('Deseja continuar? ')).strip().upper()[0]
    if flag == 'N':
        break

print(f'''Compra finalizada!
O valor total da compra foi de R${total},00;
Você comprou {caros} produtos mais caros que R$1000,00;
E o produto mais barato comprado foi {maisbarato}.
''')



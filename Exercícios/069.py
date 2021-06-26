voltas = 0
maiores = 0
homens = 0
femsub20 = 0
flag = 'S'

while True:
    voltas += 1
    sexo = str(input(f'Sexo {voltas}: ')).strip().upper()[0]
    idade = int(input(f'Idade {voltas}: '))

    if idade > 18:
        maiores += 1
    elif sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        femsub20 += 1
    
    flag = str(input('Deseja continuar? ')).strip().upper()[0]
    if flag == 'N':
        break

print(f'''Seu programa achou os seguintes resultados:
{maiores} pessoas com mais de 18 anos;
{homens} pessoas do sexo masculino;
{femsub20} mulheres abaixo dos 20 anos.
''')
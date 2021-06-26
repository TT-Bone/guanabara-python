print('-=' * 10, 'Leitor de números', '-=' * 10)

contador = soma = 0

while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    contador += 1
    soma += num

print(f'Você digitou {contador} números, e soma deles foi igual a {soma}.')

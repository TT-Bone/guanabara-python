'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''

lista = []

# Dando 5 voltas para registrar o valor da lista.
for cont in range(0, 5):
    num = int(input(f'Valor {cont + 1}: '))
    
    # Se for a primeira volta do laço, ele vai adicionar o valor direto à lista.
    if cont == 0:
        lista.append(num)
        print(f'O valor {num} foi o primeiro número a ser adicionado.')
    
    # Se o valor for maior do que o maior valor dentro da lista, ele adiciona direto ao final.
    elif num > max(lista):
        lista.append(num)
        print(f'O valor de {num} foi adicionado na posição {cont}.')
    
    # Aqui ele vai fazer a análise de cada elemento já posto dentro da lista. 
    else:
        for valor in lista:
            # O Programa vai substituir o valor que está sendo analisado dentro da lista, caso o "num" digitado seja menor ou igual a ele. Caso contrário, ele seguirá a análise até achar um número que seja maior que ele.
            if num <= valor:
                print(f'O valor {num} é menor que {valor}, e por isso será adicionado na posição {lista.index(valor)}.')
                
                lista.insert(lista.index(valor), num) 
                break
        
print(f'A lista toda de números digitados foi: {lista}')


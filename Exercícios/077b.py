tupla = (str(input('Texto 1: ')).strip(),
        str(input('Texto 2: ')).strip(),
        str(input('Texto 3: ')).strip(),
        str(input('Texto 4: ')).strip())

for txt in tupla:
    print(f'\n{txt}: ', end = '')
    for letra in txt:
        if letra in 'aeiou':
            print(f'{letra}', end = ' ')
            
'''
Um código mais simples, e mais curto. Fiz da forma como o Guanabara ensinou. O que foi interessante. A diferença aqui é que cada letra vai ser impressa repetidas vezes. No exemplo da versão 1, o programa só imprime uma única vez, mesmo que a vogal se repita por várias vezes.
Não houve a necessidade de criação de mais uma tupla para conferir quais são os itens a serem conferidos. Isso foi incluído na linha 9, dentro do IF.
'''

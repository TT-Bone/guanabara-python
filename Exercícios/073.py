'''
Crie uma tupla preenchida com 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
1. Apenas os 5 primeiros colocados.
2. Os últimos 4 colocados da tabela.
3. Uma lista com tomes em ordem alfabética.
4. Em que posição na tabela está o time da Chapecoense.
'''

time = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará-SC', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife', 'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')

# Nessa tabela do Brasileirão não consta o Chapecó. Por isso, eu farei uma adaptação e melhoramento ao comando. Ao invés de procurar o Chapecoense e não achar, vou permitir ao usuário que busque um time.
print(f'''1. Quatro primeiros colocados: \033[031m{time[:5]}\033[m.
2. Quatro ultimos colocados: \033[032m{time[-4:]}\033[m.
3. Lista em Ordem Alfabética: \033[033m{sorted(time)}\033[m.''')

while True:
    busca = str(input('4. Qual time você está buscando? '))
    if busca in time:
        print(f'O time do \033[34m{busca}\033[m está atualmente na posição \033[34m{time.index(busca) + 1}\033[m.')
        break
    else:
        print('Esse time não está nessa tabela, ou você digitou errado. Tente outro.')

print('Fim.')
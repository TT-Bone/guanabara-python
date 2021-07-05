'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços organizando os dados em forma tabular.
'''
tupla = ('Panquecas', 5.50, 'Waffles', 4.30, 'Ovos e Bacon', 6.30, 'Linguiça e BatataRosti', 7.40, 'Omelete', 4.40, 'Cheese Burger', 8.80)

# Achando uma forma para diagramar no formato tabulado os nomes.
# nome = 'Thiago'
# print(f'{nome:.<10}{nome:.>30}') 

# Ainda estava no pensamento de conseguir entregar o resultado de números pares e ímpares no intervalo de 0 ao len(tupla). Esse teste aqui, era para conseguir entregar a primeira metade dos números.
# for comida in range(0, int(len(tupla)/2)):
#     print(comida)

# Essa foi o estudo para conseguir entregar os apenas os índices PARES da contagem. A ideia era de usar dois contadores assim, um para os pares e outro para os ímpares.
# for comida in range(2, int(len(tupla) + 1), 2):
#     print(comida)

# Aqui seria a parte dos índices ÍMPARES dessa sequência.
# for comida in range(1, int(len(tupla)), 2):
#     print(comida)

# E aqui eu queria entregar as posições, sem ser índice, da primeira metade.
# for volta in range(1, int(len(tupla)/2)+1):
#     print(volta)

par = 0
impar = 1

print('=' * 52)
print(f'{"LOJAS BATMAN":^52}')
print('=' * 52)
while True:
    print(f'{tupla[par]:.<45}', end ='')
    print(f'R$ {tupla[impar]:.2f}')
    par += 2
    impar += 2
    if par == 12:
        break
print('=' * 52)
'''
Deixei todos os testes que eu fiz para conseguir achar os valores que eu estava buscando. No final das contas, eu esqueci que poderia usar algumas variáveis para fazer de controle. Porém, foram tentativas bem úteis, no final das contas. Por isso resolvi não deletar.
No final das contas, a resolução ficou super enxuta, e beem diferente do que eu imaginei que seria.
'''
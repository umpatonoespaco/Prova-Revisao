#produtos = {
#    'Maçã' : 6.39,
#    'Cenoura' : 1.19,
#    'Alface' : 4.99,
#    'Refrigerante' : 9.49,
#    'Feijão' : 4.95
#}

produtos = {}
soma = []

for i in range(5):
    chave = str(input('Insira o nome do produto: \n'))
    valor = float(input('Insira o valor do produto: \n'))

    produtos[chave] = valor

    soma.append(valor)

    print(f'Produtos no momento: {produtos}')

print(f'Produtos e seus preços: \n {produtos}')
print(f'Preço total: {sum(soma)}R$')
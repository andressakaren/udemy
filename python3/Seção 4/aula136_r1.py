# lista = []
# for numero in range(10):
#     lista.append(numero)
# print(lista)

######## List comprehension = criar listas de forma mais rápida para cirar listas a partir de iteraveis.

# lista = [
#     numero * 2
#     for numero in range(10)
# ]
# print(lista)

####### Mapeamento de dados em list comprehension
import pprint

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    # produto['nome']
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(*produtos, sep='\n')
# print(*novos_produtos, sep='\n')

pprint.pprint(novos_produtos)
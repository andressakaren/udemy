"""
Exiba os índices da lista e o conteudo
"""

lista = ['Maria', 'João', 'Luiz']
i = 0
# lista.pop()
# lista.append('Andre')
lista.insert(1, 'Andres')
del(lista[0])

for nome in lista:
    print(f'{i} {nome}')
    i += 1
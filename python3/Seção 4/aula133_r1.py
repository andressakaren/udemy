# lista = [4, 88, 9 , 5, 6, 345, 5]
# lista.sort(reverse=True)

# print(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordena(item):
    # print('PRINT', item)
    # return item['nome']

# lista.sort(key=ordena) # passar só a definição de função, não ela executada

# for item in lista:
#     print(item)
    
    
###### Função lambda
## sort
# lista.sort(key=lambda item: item['nome'])

# for item in lista:
#     print(item)

## sorted
def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

print(lista)
print()
exibir(l1)
exibir(l2)
"""
  Função que encontra o primeiro duplicado em uma lista, considerando a segunda
  ocorrência como a duplicação.

  Argumentos:
    lista_de_inteiros: Uma lista de números inteiros.

  Retorno:
    O primeiro número duplicado encontrado na lista. Se nenhum duplicado for
    encontrado, retorna -1.
  """
  
lista_de_listas_de_inteiros = [
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
  [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
  [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
  [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
  [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
  [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
  [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
  [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
  [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
  [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def encontrar_duplicado_lista(lista_de_inteiros):
    primeiro_repetido = -1
    numeros_verificados = set()
    for numero in lista_de_inteiros:
        if numero in numeros_verificados:
            primeiro_repetido = numero
            break
        numeros_verificados.add(numero)
    return primeiro_repetido

for lista in lista_de_listas_de_inteiros:
    encontrar_duplicado_lista(lista)
    print(lista, encontrar_duplicado_lista(lista))
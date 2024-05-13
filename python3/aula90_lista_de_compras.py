"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os
lista_formada = []

while True:
    resposta = input(
'''Selecione uma opção:
[i] - Inserir
[l] - Listar
[a] - Apagar
[s] - Sair
''').lower()
    
    if resposta == 'i':
        os.system('cls')
        item = input('Insira um item: ')
        lista_formada.append(item)
    
    elif resposta == 'a':       
        item_apagar = input('Qual item deseja apagar: ')
        try:
            item_apagar_int = int(item_apagar)
            del(lista_formada[item_apagar_int-1])
        except ValueError:
            print('Selecione um índice válido') 
        except IndexError:
            print('Esse índice não existe na lista') 
        except Exception:
            print('Erro desconhecido') 
    
    elif resposta == 'l':
        os.system('cls')
        if len(lista_formada) == 0:
            print('Nada para listar')
        
        for cada_item in enumerate(lista_formada):
            indice, conteudo = cada_item
            print(indice+1, conteudo)
    
    elif resposta.startswith('s'):
        print('Finalizando programa...')
        print('Finalizado')
        break
                 
    else: 
        print('escolha entre [i] - Inserir; [l] - Listar; [a] - Apagar;')   
             
    
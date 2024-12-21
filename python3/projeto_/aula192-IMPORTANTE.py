# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os

def listar(tarefas):
    print()
    if not tarefas: # uma lista vazia retorna false
        print('Nenhuma tarefa para listar!')
        print()
        return # parar a execução da função
    
    print('Tarefas:')
    for i, tarefa in enumerate(tarefas, 1):
        print(f'{i}. {tarefa}')
    print()
      
          
def desfazer(tarefas, tarefas_undone):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer!')
        print()
        return
    
    tarefa = tarefas.pop()  
    tarefas_undone.append(tarefa)  
    print(f'Tarefa desfeita: {tarefa}')
    print()
    
def refazer(tarefas, tarefas_undone):
    print()
    if not tarefas_undone:
        print('Nenhuma tarefa para refazer!')
        print()
        return
    
    # processo contrário do trecho desfazer 
    tarefa = tarefas_undone.pop()  
    tarefas.append(tarefa) 
    print(f'Tarefa refeita: {tarefa}')
    print()
  
def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nenhuma tarefa!')
        print()
        return
    
    if tarefa in tarefas:
        print(f'A tarefa "{tarefa}" já existe!')
        return
    
    print(f'Tarefa adicionada: "{tarefa}"')
    tarefas.append(tarefa)
    print()

tarefas = []
tarefas_undone = []

while True:
    print('Comandos: listar, desfazer, refazer, limpar')
    tarefa = input('Digite uma tarefa ou comando: ')
    
    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_undone)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_undone)
        listar(tarefas)
        continue
    elif tarefa == 'limpar':
        os.system('clear')
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue
        
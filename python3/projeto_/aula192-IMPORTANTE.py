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
import json

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
    
    tarefas.append(tarefa)
    print(f'Tarefa adicionada: "{tarefa}"')
    print()
    
def limpar_tela():
    os.system('clear')
    
def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados   
        
def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    
def main():
    CAMINHO_ARQUIVO = 'aula192.json'
    tarefas = ler([], CAMINHO_ARQUIVO)
    tarefas_undone = []
    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: (desfazer(tarefas, tarefas_undone), listar(tarefas)),
        'refazer': lambda: (refazer(tarefas, tarefas_undone), listar(tarefas)),
        'limpar': limpar_tela
    }

    while True:
        print('Comandos: listar, desfazer, refazer, limpar, sair')
        comando = input('Digite uma tarefa ou comando: ').strip().lower()
        
        if comando == 'sair':
            print('Encerrando... Até logo!')
            break
        elif comando in comandos:
            comandos[comando]()
        else:
            adicionar(comando, tarefas)
            listar(tarefas)
            
        salvar(tarefas, CAMINHO_ARQUIVO)  
        
if __name__ == '__main__':
    main()
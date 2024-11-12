import json

caminho_arquivo = 'aula207_a.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Joao', 23)
p2 = Pessoa('Maria', 15)
p3 = Pessoa('Luana', 50)

bd = [vars(p1), vars(p2), vars(p3)]

# Pode adiar a execução do dump envolvendo numa função 
def fazer_dump():
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        print('Fazendo o dump.....')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)
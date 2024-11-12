import json
from aula207_a import caminho_arquivo, Pessoa, fazer_dump
# Chamar a função do outro arquivo importado
fazer_dump()

with open(caminho_arquivo, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])
    print(p1.nome)
    print(p2.nome)
    print(p3.nome)
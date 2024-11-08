perguntas = [
{
'Pergunta': 'Qual é a capital da França?',
'Opções': ['Berlim', 'Roma', 'Paris', 'Madrid'],
'Resposta': 'Paris'
},
{
'Pergunta': 'Qual é o maior país do mundo em área?',
'Opções': ['Rússia', 'China', 'Canadá', 'Estados Unidos'],
'Resposta': 'Rússia'
},
{
'Pergunta': 'Em qual continente fica o Egito?',
'Opções': ['África', 'Europa', 'Ásia', 'América do Sul'],
'Resposta': 'África'
},
{
'Pergunta': 'Qual é o maior oceano do mundo?',
'Opções': ['Oceano Atlântico', 'Oceano Índico', 'Oceano Pacífico', 'Oceano Ártico'],
'Resposta': 'Oceano Pacífico'
},
{
'Pergunta': 'Qual é a montanha mais alta do mundo?',
'Opções': ['K2', 'Kangchenjunga', 'Lhotse', 'Monte Everest'],
'Resposta': 'Monte Everest'
}
]
count = 0
for i, pergunta in enumerate(perguntas):
    print(f'{i+1})', pergunta['Pergunta'])
    print()
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i+1})', opcao)
    print()
    
    resposta = input('Digite sua escolha: ')
    print()
    
    # Validar resposta = digito inteiro
    acertou = False 
    resposta_num_inteiro = None
    qntd_opcoes = len(opcoes)
    
    if resposta.isdigit():
        resposta_num_inteiro = int(resposta) - 1
        
    if resposta_num_inteiro is not None:
        
    # Se o numero digitado está entre as opções
        if resposta_num_inteiro >= 0 and resposta_num_inteiro < qntd_opcoes:
            if opcoes[resposta_num_inteiro] == pergunta['Resposta']:
                acertou = True
                
    if acertou:
        count += 1
        print('Acertou')
    else:
        print('Errou')   
    print()
    
print(f'Você acertou {count} questoes de {len(perguntas)}')
perguntas = [
{
'Pergunta': 'Quem é o vocalista da banda Queen?',
'Opções': ['Freddie Mercury', 'John Lennon', 'David Bowie', 'Elvis Presley'],
'Resposta': 'Freddie Mercury'
},
{
'Pergunta': 'Qual é o nome do álbum de estreia dos Beatles?',
'Opções': ['Abbey Road', 'Sgt. Peppers Lonely Hearts Club Band', 'Please Please Me', 'Rubber Soul'],
'Resposta': 'Please Please Me'
},
{
'Pergunta': 'Qual é o instrumento musical que Michael Jackson tocava?',
'Opções': ['Bateria', 'Guitarra', 'Violino', 'Saxofone'],
'Resposta': 'Bateria'
},
{
'Pergunta': 'Em qual ano o festival Woodstock aconteceu?',
'Opções': ['1967', '1969', '1971', '1973'],
'Resposta': '1969'
},
{
'Pergunta': 'Qual é o nome do primeiro álbum solo de Paul McCartney?',
'Opções': ['McCartney', 'Band on the Run', 'Tug of War', 'Pipes of Peace'],
'Resposta': 'McCartney'
}
]

count = 0
for i, pergunta in enumerate(perguntas):
    print(f'Questão {i+1})', pergunta['Pergunta'])
    print()
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i+1}) {opcao}')
    print()
    
    resposta = input('Digite uma resposta: ')
    print()
    
    resposta_num_inteiro = None
    qntd_opcoes = len(opcoes)
    acertou = False
    
    if resposta.isdigit():
        resposta_num_inteiro = int(resposta) - 1
        
    if resposta_num_inteiro is not None:
        if resposta_num_inteiro >= 0 and resposta_num_inteiro < qntd_opcoes:
            if opcoes[resposta_num_inteiro] == pergunta['Resposta']:
                acertou = True

    if acertou:
        count += 1
        print('Você acertou!!')
    else:
        print('Você errou!!')
    print()
    
print(f'Você acertou {count} questões de {len(perguntas)}!!')
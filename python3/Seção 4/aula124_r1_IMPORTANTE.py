perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

count = 0
for pergunta in perguntas:
    print('Pergunta:' , pergunta['Pergunta'])
    print()
    
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)    
    print()
    
    escolha = input('Escolha uma opção: ')
    
    acerto = False # Não acertou ainda
    escolha_int = None
    qtd_opcoes = len(opcoes)
    
    # converter para inteiro
    if escolha.isdigit():
        escolha_int = int(escolha)
        
    if escolha_int is not None:
        # Saber se existe dentro da lista
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acerto = True     
    print()      
    if acerto:
        count += 1
        print('Acertou')
    else:
        print('Errou')     
    print()
    
print(f'Você acertou {count},')
print(f'de {len(perguntas)} perguntas.')
    


    
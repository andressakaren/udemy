"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

secret_word = "cachorro"
i = 0 # Número de tentativas
letras_acertadas = ''

while True:
    resposta = input('Pensei em uma palavra. Tente advinhar. Digite uma letra: ').lower()
    i += 1
    
    # condições erradas
    if len(resposta) > 1:
        print('Você digitou mais de uma letra!')
        continue
    if resposta in '0123456789':
        print('Você digitou um número!!') 
        continue
     
    # condições certas
    if resposta in secret_word: 
        letras_acertadas += resposta # salvar as letras acertadas
    
    palavra_formada = '' # salvar a palavra formada (concatenada)
    for letra in secret_word:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    print(palavra_formada)
    
    if palavra_formada == secret_word:
        os.system('cls')
        print(f'VOCÊ VENCEU!! \nA palavra que pensei era {secret_word}. \nVocê utilizou {i} Tentativas. ')
        break

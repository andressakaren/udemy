"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input('Digite seu primeiro nome: ')
tamanho = len(primeiro_nome)
curto = tamanho <= 4
normal = 5 <= tamanho <= 6
grande = tamanho > 6 

if tamanho > 1:
    if curto:
        print("Seu nome é curto")
    elif normal:
        print("Seu nome é normal")
    elif grande:
        print("Seu nome é muito grande")
else:
    print("Digite mais de uma letra.")        
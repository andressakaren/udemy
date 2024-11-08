# Letra com maior quantidade de repetição na frase

frase = input('Digite uma frase: ')
i = 0
qnt_vezes_inicial = 0 
qnt_vezes = 0
letra = ''

while i < len(frase):
    letra_atual = frase[i]
    qnt_vezes = frase.count(letra_atual)
    
    if letra_atual == ' ':
        i += 1
        continue
    
    if qnt_vezes_inicial < qnt_vezes:
        qnt_vezes_inicial = qnt_vezes
        letra = letra_atual
    i += 1
    
print(f'A letra que aperceu mais vezes foi "{letra}", um total de {qnt_vezes_inicial}x')    
     


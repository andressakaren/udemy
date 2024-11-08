# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicacao(*args):
    #evitar multiplicação por 0
    total = 1
    for num in args:
        total *= num
    return total
    
result = multiplicacao(10,2,3,4,5)
print(result)

def par_impar(numero):
    return numero % 2 == 0

print(par_impar(2))
print(par_impar(24))
print(par_impar(21))
print(par_impar(3))
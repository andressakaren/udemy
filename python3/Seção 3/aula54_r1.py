"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_inteiro = int(input("Digite um número inteiro: "))

numero_inteiro_par = numero_inteiro % 2 == 0
numero_inteiro_impar = numero_inteiro % 2 != 0

if numero_inteiro_par:
    print("Este número é par.")
elif numero_inteiro_impar:
    print("Este número é ímpar.")
else:
    print("Não digitou um número inteiro!")
    

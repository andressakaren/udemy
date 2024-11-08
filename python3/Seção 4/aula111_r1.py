"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# desempacotamento 
x, y, *resto = 1, 2 ,3, 4, 5
print(x, y, resto)

# def soma(x, y):
#     return x + y 

def soma(*args):
    total = 0
    for numero in args:
        # print('Total', total, numero)
        total += numero
        # print('Total', total)
    return total

soma1 = soma(1,2,3,4,5,6)

print(soma1)
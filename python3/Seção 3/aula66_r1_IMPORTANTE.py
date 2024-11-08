while True:
    
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+ - / *): ')
    
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    
    # Try and except para poder analisar se os numeros são válidos 
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print(f'Um ou ambos os números digitados são inválidos!')
        continue
    
    # Verificar se os operadores são permitidos
    operadores_permitidos = '+-/*'
      
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue  
    
    # Operações 
    print(f'Realizando sua conta. Confira o resultado abaixo: ')
    if operador == '+':
        print(f'{numero_1} + {numero_2} = {num_1_float + num_2_float}')
    elif operador == '-':
        print(f'{numero_1} - {numero_2} = {num_1_float - num_2_float}')
    elif operador == '*':
        print(f'{numero_1} * {numero_2} = {(num_1_float * num_2_float):.2f}')
    elif operador == '/':
        print(f'{numero_1} / {numero_2} = {(num_1_float / num_2_float):.2f}')   
    else:
        print(f'Não era pra chegar aqui nunca kk')  
       
    sair = input('Quer sair? [s]').lower().startswith('s')
    if sair:
        break

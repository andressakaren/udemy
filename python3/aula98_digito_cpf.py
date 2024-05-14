while True:
    cpf = input('Digite o seu cpf: ')
    if len(cpf) != 11:
        print('Insira um cpf com 11 dígitos para ser válido')
        continue
    try:
        cpf in '0123456789'       
    except: 
        print('Você digitou valores inválidos')
        
    # colocar somente os 9 digitos numa lista
    nove_digitos = cpf[:9]

    # multiplicar por contagem regressiva começando por 10 até 2 e somar resultado entre o si
    resultado_dig_1 = 0
    contador_regressivo_1 = 10
    for digito in nove_digitos:
        resultado_dig_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1  

    # multiplicar por 10 e pegar o resto da div 11
    vezes_10 = resultado_dig_1 * 10
    resto_div_11 = vezes_10 % 11

    # condições validação 
    digito_1_correto = 0
    if resto_div_11 > 9:
        digito_1_correto = 0
    else:
        digito_1_correto = resto_div_11
        
    print(f'O valor do primeiro dígito é: {digito_1_correto}')
        
  
    
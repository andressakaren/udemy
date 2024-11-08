import random

for cem in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0,9))

    ### PRIMEIRO DÍGITO
        
    resultado_dig1 = 0
    contador_regressivo_1 = 10
    for digito in nove_digitos:
        resultado_dig1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1  

    vezes10_dig1 = resultado_dig1 * 10
    resto_div11_dig1 = vezes10_dig1 % 11

    digito1_correto = 0
    if resto_div11_dig1 > 9:
        digito1_correto = 0
    else:
        digito1_correto = resto_div11_dig1
        
    ### SEGUNDO DÍGITO

    dez_digitos = nove_digitos + str(digito1_correto)
    resultado_dig2 = 0
    contador_regressivo_2 = 11
    for digito in dez_digitos:
        resultado_dig2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1  

    vezes10_dig2 = resultado_dig2 * 10
    resto_div11_dig2 = vezes10_dig2 % 11

    digito2_correto = 0
    if resto_div11_dig2 > 9:
        digito2_correto = 0
    else:
        digito2_correto = resto_div11_dig2
        
        
    ### GERADOR DE CPF

    cpf_gerado_pelo_calculo = (f'{nove_digitos}{digito1_correto}{digito2_correto}')
    print(cpf_gerado_pelo_calculo)

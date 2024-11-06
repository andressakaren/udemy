caminho_arquivo = 'aula188.txt'

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:  
    arquivo.write('Atenção\n')
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(                      
        ('linha 3\n', 'linha 4\n')
    )

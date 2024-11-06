# Abrir um arquivo criando ele.
# r (leitura), w (escrita), x (para criação), a (escreve ao final), b (binario), t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)

# METODOS UTEIS
# write, read (escrever e ler)
# writelines (escrever varias linhas)
# readline 
# readlines 

caminho_arquivo = 'aula187.txt'

# print(caminho_arquivo)

# arquivo = open(caminho_arquivo, 'w')
# # Fechar
# arquivo.close()

with open(caminho_arquivo, 'w+') as arquivo:  # arquivo é a variável
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(                       # só recebe iterável
        ('linha 3\n', 'linha 4\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    
    print('Lendo...')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='') # print ssempre tem uma quebra de linha, pra evitar conflito com o \n, usar ou o end ou o .strip
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print(arquivo.readline())
    
    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())

print('#' * 10)

with open(caminho_arquivo, 'r') as arquivo:  # arquivo é a variável
    print(arquivo.read())

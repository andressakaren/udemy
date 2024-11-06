# Abrir um arquivo criando ele. 
# r (leitura), w (escrita), x (para criação), a (escreve ao final), b (binario), t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)

# METODOS UTEIS


# colocar duas \\ para evitar escape
caminho_arquivo = 'C:\\Users\\andre\\OneDrive\\Documentos\\GitHub\\udemy\\python3\\projeto_\\'
caminho_arquivo += 'aula186.txt'

# print(caminho_arquivo)

# arquivo = open(caminho_arquivo, 'w')
# # Fechar
# arquivo.close()

with open(caminho_arquivo, 'w') as arquivo: # arquivo é a variável
    print('Olá mundo')
    print('Arquivo vai ser fechado')
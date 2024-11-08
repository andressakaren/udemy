# Crie funções que duplicam, triplicam e quadriplicam o número recebido como parâmetro

num = int(input('Digite o número: '))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(num))
print(triplicar(num))
print(quadruplicar(num))

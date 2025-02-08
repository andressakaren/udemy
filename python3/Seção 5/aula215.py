# associaçãoligação de um objeto para outro objeto

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        # método protegido
        self._ferramenta = None
    
    @property # permitir leitura     
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter # permite modificação 
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta
        
class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome
    
    def escrever(self):
        return f'{self.nome} está escrevendo...'        

# e1 = Escritor('luuis')
# f1 = FerramentaDeEscrever('caneta Bic') 
# e1.ferramenta = 'caneta' # atribuição de um avalor a variavel ferramenta
# print(e1.ferramenta)
# e1.ferramenta = 'lapis'
# print(e1.ferramenta)
# print(f1.escrever())


# atribuir um valor ao setter
# e1.ferramenta = 'caneta'
# print(e1.ferramenta)


escritor = Escritor('Luis')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_escrever = FerramentaDeEscrever('Maquina')
# escritor.ferramenta = caneta # associação 
escritor.ferramenta = maquina_escrever

print(caneta.escrever())
print(maquina_escrever.escrever())
print(escritor.ferramenta.escrever())




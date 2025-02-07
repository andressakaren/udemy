class Escritor:
    def __init__(self, nome):
        self.nome = nome
        # método protegido
        self._ferramenta = None
    
    @property # permitir leitura     
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta
        
class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome
        

e1 = Escritor('luuis')
f1 = FerramentaDeEscrever('caneta Bic')

# atribuir um valor ao setter
# e1.ferramenta = 'caneta'
# print(e1.ferramenta)



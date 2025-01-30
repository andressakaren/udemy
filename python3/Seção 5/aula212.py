class Caneta:
    def __init__(self, cor):
        #private protected
        self._cor = cor
        self._cor_tampa = None
        
    @property
    def cor(self):
        print('Property')
        return self._cor
    
    # @property
    # def cor_tampa(self):
    #     print('executando..')
    #     return 12345

    @cor.setter
    def cor(self, valor):
        print('Está no setter')
        if valor == 'rosa':
            raise ValueError('Não aceito a cor rosa')
        self._cor = valor
        return self._cor
    
    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor
    
caneta = Caneta('Azul')
# getter --> obter valor 
print(caneta.cor)

caneta.cor = 'pink'
print(caneta.cor)
print(caneta.cor)
caneta.cor_tampa = 'aamarelo'
print(caneta.cor_tampa)


# Métodos em instâncias de classes em Python 
# Hard coded - algo que foi escrito diretamente no codigo
# Classe é o molde - (geralmente sem dados)
# Instância da classe (instancia ou objeto) - Tem dados 
# Uma classe pode gerar vários objetos 
# Na classe o self é a própria instancia. 

class Carro:
    def __init__(self, nome):
        self.nome = nome  
        
    def acelerar(self):
        print(f'{self.nome} está acelerando....')
    
fusca = Carro('fusca')
print(fusca.nome)
fusca.acelerar()
    
celta = Carro(nome='celta')
print(celta.nome)
celta.acelerar()

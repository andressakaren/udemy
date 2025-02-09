# Composição é uma especialização da agregação
# Quando um objeto "pai" for apagado, todas as referencias dos objetos filhos tbm serão apagadas 

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
        
    def inserir_enderecos(self, rua, numero):
        # criar endereço a partir da classe 
        self.enderecos.append(Endereco(rua, numero))

    def inserir_enderecos_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
    
    def __del__(self):
        print('APAGANDO', self.nome)
    
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
        
    def __del__(self):
        print('APAGANDO', self.rua, self.numero)    

cliente1 = Cliente('Maria')
cliente1.inserir_enderecos('Rua Candido,', 234)
cliente1.inserir_enderecos('Rua David Caldas,', 1090)

endereco_externo = Endereco('Av Piaui', 200)
cliente1.inserir_enderecos_externo(endereco_externo)
cliente1.listar_enderecos()

del cliente1

print(endereco_externo.rua, endereco_externo.numero)

print('***** ENCERRANDO O CÓDIGO')





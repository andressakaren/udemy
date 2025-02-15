# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class


# class object
# todas as classes já herdam do buitins object do python 

# MRO -Method Resolution Order

class Pessoa:
    cpf = '12354'
    
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
    def falar_nome_classe(self):
        print('Classe Pessoa')
        print(self.nome, self.sobrenome, self.__class__.__name__)
        
class Cliente(Pessoa): # Cliente extende pessoas
    def falar_nome_classe(self):
        print('ESTA NA CLASSE CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)
    
    
class Aluno(Pessoa):
    cpf = '12354 ALUNO'
    ...
    
c1 = Cliente('Andressa', 'Karen')
c1.falar_nome_classe()
# essa resposta é pq acessa primeiro a classe cliente, devido ao MRO. Resposta:

# ESTA NA CLASSE CLIENTE
# Andressa Karen Cliente

a1 = Aluno('Luis', 'Otavio')
a1.falar_nome_classe()

print(a1.cpf)
print(a1.cpf)
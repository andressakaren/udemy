class Pessoa:
    ano = 2023 
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(self):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anonimo', idade)
    
    
p1 = Pessoa('Joao', 34)
p2 = Pessoa.criar_com_50_anos('maria')
p3 = Pessoa.criar_sem_nome(88)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
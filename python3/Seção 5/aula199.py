# Class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que podem ter seus proprios atributos e métodos. 
# Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações. 
# Por convençao, usamos PascalCase para nomes de classes. 

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
p1 = Pessoa('Luiz', 'Eduardo')
p2 = Pessoa('Maria', 'Paula')

print(p1.nome, p1.sobrenome)
print(p2.nome, p2.sobrenome)


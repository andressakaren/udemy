# Crie uma classe Animal que tenha os atributos nome e idade.

# Ela deve ter um método emitir_som() que retorna "O animal faz um som."
# Crie classes Cachorro e Gato que herdam de Animal.

# Cachorro deve sobrepor emitir_som() para retornar "O cachorro late."
# Gato deve sobrepor emitir_som() para retornar "O gato mia."
# Crie uma classe Dono que representa o dono do animal.

# Deve ter um atributo nome e um método apresentar_animal(animal) que imprime o nome do animal e o som que ele faz.
# Crie instâncias de Cachorro e Gato, associe a um dono e exiba os detalhes.


class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def emitir_som(self):
        return f"Um animal faz um som."
    
class Cachorro(Animal):
    def emitir_som(self):
        return f'O cachorro late'
    
    
class Gato(Animal):   
    def emitir_som(self):
        return f'O gato mia'    
    
class Dono:
    def __init__(self, nome):
        self.nome = nome
        
    def apresentar_animal(self, animal):
        print(f'{self.nome} tem um {type(animal).__name__} chamado {animal.nome}')
        print(f'{animal.nome} diz: {animal.emitir_som()}\n')
    
    
cachorro = Cachorro('bely', 10)
# print(cachorro.emitir_som())

gato = Gato('Ulla', 3)

dono = Dono('Ddl')
dono.apresentar_animal(cachorro)
dono.apresentar_animal(gato)
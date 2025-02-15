# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, nome_motor):
        self._motor = nome_motor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, nome_fabricante):
        self._fabricante = nome_fabricante

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome


# criar carro
fusca = Carro('Fusca')
uno = Carro('Uno')
hilux = Carro('Hilux')
# criar fabricante
volkswagen = Fabricante('Volkswagen')
fiat = Fabricante('Fiat')
toyota = Fabricante('Toyota')
# criar motor
motor_1_0 = Motor('1.0')
motor_2_0 = Motor('2.0')


fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

uno.fabricante = fiat
uno.motor = motor_1_0
print(uno.nome, uno.fabricante.nome, uno.motor.nome)

hilux.fabricante = toyota
hilux.motor = motor_2_0
print(hilux.nome, hilux.fabricante.nome, hilux.motor.nome)


# MINHA SOLUÇÃO

# class Carro:
#     def __init__(self, nome):
#         self.nome = nome
        
#     def adcionar_motor(self, motor):
#         return f'Adcionado motor {motor.nome} ao carro {self.nome}!!'
    
        
# class Motor:
#     def __init__(self, nome):
#         self.nome = nome
        
        
# class Fabricante:
#     def __init__(self, nome):
#         self.nome = nome
#         self.lista_carros = []
        
#     def fabricar_carro(self, nome_carro):
#         carro = Carro(nome_carro)
#         self.lista_carros.append(carro)
#         return carro
        
#     def listar_carros_fabricados(self):
#         print('Carros Fabricados:')
#         for carro in self.lista_carros:
#             print(f'Carro: {carro.nome}\nMotor: ')
        
# # carro1 = Carro('Corolla')
# # carro2 = Carro('HB20')
# motor_turbo = Motor('Turbo')
# motor_4x4 = Motor('4x4')

# # carro1.adcionar_motor(motor_turbo)
# # carro2.adcionar_motor(motor_turbo)

# # print(carro1.adcionar_motor(motor_turbo))
# # print(carro2.adcionar_motor(motor_turbo))

# toyota = Fabricante('Toyota')

# ltriton = toyota.fabricar_carro('Ltriton')
# hilux = toyota.fabricar_carro('Hilux')

# # print(ltriton.adcionar_motor(motor_turbo))

# toyota.listar_carros_fabricados()

# print(ltriton.adcionar_motor(motor_turbo))
# print(hilux.adcionar_motor(motor_4x4))
        
    
class A(object):
    atributo_a = 'Valor A'
    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'Valor B'
    
    def __init__(self, atributo):
        super().__init__(atributo)

    # def __init__(self, atributo):
    #     self.atributo = atributo

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'Valor C'

    # def __init__(self):
    #     self.atributo = atributo

    def metodo(self):
        # super(A, self).metodo() # ERRO tipo, eu sou o B e meu objeto é o self.
        # super(B, self).metodo() # tipo, eu sou o B e meu objeto é o self.
        # super(C, self).metodo() # tipo, eu sou o C e meu objeto é o self.
        print('C')
     
c = C('atributo')   
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)

# c.metodo()
print(c.atributo)

# print(C.mro())
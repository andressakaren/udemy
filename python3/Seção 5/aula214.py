# abstração, heraça, encapsulamento e polimorfismo 

class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__exemplo = 'isso é PRIVADO'
        
    def metodo_publico(self):
        # self._metodo_protegido()
        self.__metodo_privado()
        print(self.__exemplo)
        return 'metodo_publico'
    
    def _metodo_protegido(self):
        print('metodo protegido')
        return '_metodo_protected'
    
    def __metodo_privado(self):
        print('__metod_privado')
        return '__metodo_privado'
    
f = Foo()
print(f.public)
print(f._protected)
print(f.metodo_publico())
print(f._metodo_protegido())

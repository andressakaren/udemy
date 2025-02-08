# Agregação - forma mais especiaçizada de associação entre dois ou mais objetos. Cada objeto terá seu siclo de vida independente. 
# Geralmente é uma relação de 1 para muitos, onde um objeto tem  um ou muitos objetos. 
# Os objetos podem viver separadamente, mas pode se tratar de uma relação onde um obj precia de outro para fazer determinada taefa.

# é um tipo de associação. Ainda uma relação fraca, um existe sem o outro

class Carrinho:
    def __init__(self):
        self._produtos = []
        
    def total(self):
        # precos = []
        # for p in self._produtos:
        #     precos.append(p.preco)
        # total = sum(precos)
        # return total
        return sum([p.preco for p in self._produtos])
        
    def inserir_produtos(self, *produtos): # empacotar tudo em uma tupla
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)
            
    def listar_produtos(self):
        print('Listar produtos: ')
        for produto in self._produtos:
            # cada elemento da lista é um objeto da classe Produto e consegue acessar diretamente os atributos nome e preco.
            print(produto.nome, produto.preco)
        
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        

carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)

carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())
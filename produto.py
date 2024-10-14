class Produto:
    def __init__(self, nome: str, preco: float, qtd: int):
        self.__nome = nome
        self.__preco = preco
        self.__qtd = qtd
        
    
    @property
    def nome(self):
        return self.__nome
    
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        
    
    @property
    def preco(self):
        return self.__preco
    
    
    @preco.setter
    def preco(self, novo_preco):
        self._preco = novo_preco
        
    
    @property
    def qtd(self):
        return self.__qtd
    
    
    @qtd.setter
    def qtd(self, nova_qtd):
        self.__qtd = nova_qtd
        
        
    def __str__(self):
        return f'Produto: {self.__nome} - Preço: R${self.__preco} - Quantidade: {self.__qtd}'
    
class Cliente:
    
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return.nome.title()

cliente = Cliente("Marco")
cliente2 = Cliente("Marco")
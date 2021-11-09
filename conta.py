class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ...".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} é do :{}".format(self.saldo, self.titular))

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def transferir(self, valor, origem, destino):   ##  def transferir(self, valor x, conta1 = origem, conta2 = desitino)
        self.saca(valor)
        destino.depostita(valor) 
    
    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__titular

    def get_saldo(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite
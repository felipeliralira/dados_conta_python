class Conta:
    def __init__(self, numero_conta, titular_conta, saldo_conta, limite_conta = 1000):
        self.__numero = numero_conta
        self.__titular = titular_conta
        self.__saldo = saldo_conta
        self.__limite = limite_conta

    #Declaração dos métodos (funções)
    def extrato(self):
        print(f"Saldo atual: {self.__saldo} do titular {self.__titular}")

    def depositar(self, valor):
        if self.valor < 0:
            print("Valor de depósito inválido")
        else:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado com sucesso. Saldo atual: {self.__saldo}")

    def sacar(self, valor):
        self.__saldo -= valor
        if self.__saldo < valor:
            print("Saldo insuficiente")
        else:
            print(f"Saque de {valor} realizado com sucesso. Saldo atual: {self.__saldo}")
            
    def transferir(self, valor, conta_destino):
        if (self.__saldo < valor) or (valor < 0):
            print("Valor de transferência inválido ou saldo insuficiente")
        else:
            self.sacar(valor)
            conta_destino.depositar(valor)
    
    #Métodos para retornar apenas 
    #valores das propriedades
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    @property
    def numero(self):
        return self.__numero
    
    #Métodos para manipular 
    #os valores das propriedades

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular 
    
    @limite.setter
    def limite(self, limite):
        self._limite = limite

    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    
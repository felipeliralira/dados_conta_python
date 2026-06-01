class Conta:
    def __init__(self, numero_conta, titular_conta, saldo_conta, limite_conta):
        self.__numero = numero_conta
        self.__titular = titular_conta
        self.__saldo = saldo_conta
        self.__limite_especial = limite_conta

    #Declaração dos métodos (funções)
    def extrato(self):
        print(f"Saldo atual: {self.__saldo} do titular {self.__titular}")

    def depositar(self, valor):
        if self.valor <= 0:
            print("Valor de depósito inválido")
        else:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado com sucesso. Saldo atual: {self.__saldo}")

    def __saque_permitido(self, valor_saque):
        valor_disponivel_saque = self.__saldo + self.__limite_especial
        return valor_saque <= valor_disponivel_saque

    def sacar(self, valor):
        
        if (self.__saque_permitido(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou do limite.")
            
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
        return self.__limite_especial
    
    @property
    def numero(self):
        return self.__numero
    
    @staticmethod
    def codigo_banco():
        return '001'
    
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237', 'Itaú': '341'}
    
    
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
    
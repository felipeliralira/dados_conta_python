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

#Crie uma classe que represente um vídeo com os atributos título, duração e views
class Video:
    def __init__(self, titulo, duracao, views):
        self.titulo = titulo
        self.duracao = duracao
        self.views = views

video = Video("Baleia Azul", "5:00", 10000)


# Como poderia ser criada uma classe que represente o objeto livro = Livro(titulo,autor,data_publicacao)?
class Livro:
    def __init__(self, titulo, autor, data_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.data_publicacao = data_publicacao
livro = Livro("A história do Xamã", "Eduardo Klen", "29/11/2008")
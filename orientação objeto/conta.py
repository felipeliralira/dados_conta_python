class Conta:
    def __init__(self, numero_conta, titular_conta, saldo_conta, limite_conta = 1000):
        self.numero = numero_conta
        self.titular = titular_conta
        self.saldo = saldo_conta
        self.limite = limite_conta

    #Declaração dos métodos (funções)
    def extrato(self):
        print(f"Saldo atual: {self.saldo} do titular {self.titular}")

    def depositar(self, valor):
        if self.valor < 0:
            print("Valor de depósito inválido")
        else:
            self.saldo += valor
            print(f"Depósito de {valor} realizado com sucesso. Saldo atual: {self.saldo}")

    def sacar(self, valor):
        self.saldo -= valor
        if self.saldo < valor:
            print("Saldo insuficiente")
        else:
            print(f"Saque de {valor} realizado com sucesso. Saldo atual: {self.saldo}")


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
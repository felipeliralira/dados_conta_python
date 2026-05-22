from conta import Conta

conta = Conta(123456, "João Silva", 1000.0, 2000.0)
conta1 = Conta(654321, "Maria Souza", 1500.0, 2500.0)

# Suponha que por padrão as contas criadas possuam limite inicial de 1000.0 e apenas contas especiais tem limites diferentes. Como poderiamos declarar os parametros da classe para que o codigo nao fique repetitivo

conta = Conta(123456, "João Silva", 0.0)
conta1 = Conta(654321, "Maria Souza", 0.0)
conta2 = Conta(111222, "Carlos Oliveira", 0.0, 2000.0)
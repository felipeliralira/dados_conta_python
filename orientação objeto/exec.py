from conta import Conta

conta = Conta(123456, "João Silva", 1000.0, 2000.0)
conta1 = Conta(654321, "Maria Souza", 1500.0, 2500.0)


conta.transferir(500.0, conta1)
conta.extrato()
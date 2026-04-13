numero_conta = 123456
titular = "Felipe Lira de Oliveira"
saldo = 1000.0
limite = 2000.0

conta = {
    "numero_conta": numero_conta,
    "titular": titular,
    "saldo": saldo,
    "limite": limite
}

print(conta["titular"])
print(conta["limite"])

def criar_conta(numero_conta, titular, saldo, limite):
    conta = {
        "numero_conta": numero_conta,
        "titular": titular,
        "saldo": saldo,
        "limite": limite
    }
    return conta

conta = nova_conta = criar_conta(654321, "Maria Souza", 1500.0, 2500.0)
print(conta["limite"])

def depositar(conta, valor):
    conta["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print(f"Seu saldo atual é {conta['saldo']}")

depositar(conta, 500.0)
extrato(conta)
sacar(conta, 200.0)
extrato(conta)
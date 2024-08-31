def sacar(valor):
    saldo = 500
    if saldo >= valor:
        saldo -= valor
        print('Saque efetuado com sucesso!')
    else:
        print('Saldo insuficiente!')
    
    print('Saldo atual: R$ ' + str(saldo))
    
def depositar(valor):
    saldo = 500
    saldo += valor
    print('Depósito efetuado com sucesso!')
    print('Saldo atual: R$ ' + str(saldo))

sacar(600)
depositar(50)
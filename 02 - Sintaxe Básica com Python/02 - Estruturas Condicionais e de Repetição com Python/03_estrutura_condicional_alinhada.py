conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        saldo -= saque
        print('Saque efetuado com sucesso')
    elif (saldo + cheque_especial) >= saque:
        saldo -= saque
        print('Saque cheque especial efetuado com sucesso')
    else:
        print('Saldo insuficiente')
elif conta_universitaria:
    if saldo >= saque:
        saldo -= saque
        print('Saque efetuado com sucesso')
    else:
        print('Saldo insuficiente')
else:
    print('Tipo de conta inválido')
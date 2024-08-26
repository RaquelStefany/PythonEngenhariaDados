saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

# if
if saldo >= saque:
    saldo -= saque
    print("Saque efetuado com sucesso!")
if saldo < saque:
    print("Saldo insuficiente!")
    
print("Saldo atual: R$ " + str(saldo) + "\n")

# if / else
if saldo >= saque:
    saldo -= saque
    print("Saque efetuado com sucesso!")
else:
    print("Saldo insuficiente!")
    
print("Saldo atual: R$ " + str(saldo) + "\n")

# if / elif / else
opcao = int(input("Informe uma opção: \n[1] Sacar\n[2] Extrato:\n"))

if opcao == 1:
    saque = float(input("\nInforme o valor do saque: "))
    if saldo >= saque:
        saldo -= saque
        print("Saque efetuado com sucesso!")    
        print("Saldo atual: R$ " + str(saldo))
    else:
        print("Saldo insuficiente!")
elif opcao == 2:
    print("\nExtrato: R$ " + str(saldo))
else:
    print("\nOpção inválida!")
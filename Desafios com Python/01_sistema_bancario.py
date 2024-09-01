import os
import sys

opcao = ""
extrato = []
limite_saques = 3
saque_diario = 0
saque_maximo = 500
saldo_atual = 0

print("\nBem-vindo ao Banco\n")

def saque(valor):
    while valor <= 0:
        print("\nValor inválido.")
        valor = float(input("Digite um valor válido para saque: "))
    else:
        global saque_diario
        global saldo_atual
        global extrato
        if valor <= saldo_atual:
            if valor <= saque_maximo:
                print(f"Saque de R${valor:.2f} realizado com sucesso!\n")
                extrato.append(f"- Saque de R${valor:.2f}")
                saldo_atual -= valor
                saque_diario += 1
                menu()
            else:
                print(f"Valor de saque deve ser menor que R${saque_maximo:.2f}\n")
                menu()
        else:
            print(f"Saldo insuficiente para saque.\nSaldo atual de R${saldo_atual:.2f}\n")
            menu()

def deposito(valor):
    while valor <= 0:
        print("\nValor inválido.")
        valor = float(input("Digite um valor válido para depósito: "))
    else:
        global saldo_atual
        global extrato
        print(f"Depósito de R${valor:.2f} realizado com sucesso!\n")
        extrato.append(f"+ Depósito de R${valor:.2f}")
        saldo_atual += valor
        menu()

def exibir_extrato():
    print("\nExtrato bancário:\n")
    if extrato:
        for i in extrato:
            print(i)              
    else:
        print("Nenhuma transação realizada.")
    print(f"\nSaldo atual: R${saldo_atual:.2f}\n")
            
    input(
        "Aperte 'Enter' para sair do extrato...\n\n"
    ).upper()
    limpar_console()
    menu()  
    
def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        opcao = input(
            "Selecione uma opção:\n\n[D] Depositar\n[S] Sacar\n[E] Extrato\n[Q] Sair\n\n"
        ).upper()

        if opcao == "D":
            limpar_console()
            valor = float(input("Digite o valor do depósito: "))
            deposito(valor)
        elif opcao == "S":
            limpar_console()
            if saque_diario < limite_saques:
                valor = float(input("Digite o valor do saque: "))
                saque(valor)
            else:
                print("Limite de 3 saques diários atingido.\n")
                menu()
        elif opcao == "E":
            limpar_console()
            exibir_extrato()
        elif opcao == "Q":
            print("Saindo...\n")
            sys.exit()
        else:
            print("Opção inválida.\n")

menu()

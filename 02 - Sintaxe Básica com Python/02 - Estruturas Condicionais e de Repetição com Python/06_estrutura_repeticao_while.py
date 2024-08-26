opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar\n[2] Extrato\n[0] Sair\n"))
    
    if opcao == 1:
        print("Sacando...\n")
    elif opcao == 2:
        print("Gerando extrato...\n")
else:
    print("Saindo...\n")



while True:
    numero = int(input("Informe um número: "))
    
    if numero == 10:
        break
    
    if numero % 2 == 0:
        continue
    
    print("Você digitou o número: ", numero, "\n")
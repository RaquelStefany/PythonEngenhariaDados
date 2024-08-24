# input
nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

# output
print("\nOlá, " + nome, end="...\n")
print(f"Você tem {idade} anos de idade.")
print("E Seu nickname é", end=" ")
print(nome, idade, sep="#", end=".\n")
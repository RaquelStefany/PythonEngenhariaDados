# São operadores utilizados em conjunto com operadores de comparação, para montar uma expressão lógica.
# Quando um operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos
# combinar operadores de comparação com os operadores lógicos.

# Exemplo:
# Operador AND (E): Retorna True se ambas as expressões forem verdadeiras.
# Operador OR (Ou): Retorna True se pelo menos uma das expressões for verdadeira.
# Operador NOT (Negação): Retorna True se a expressão for falsa.

saldo = 1000
saque = 200
limite = 100

# Operador AND (E)
print(saldo >= saque and saque <= limite)

# Operador OR (Ou)
print(saldo >= saque or saque <= limite)

# Operador NOT (Negação)
print(not saldo >= saque)

# Parênteses
conta_especial = True
print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))

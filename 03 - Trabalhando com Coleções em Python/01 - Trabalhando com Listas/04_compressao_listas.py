numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

# Retornar somente valores pares com for
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)        

# Retornando somente pares com comprehension 
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

quadrado = []

# Retornar números elevando ao quadrado com for
for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado)

# Retornar números elevando ao quadrado com comprehension 
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)
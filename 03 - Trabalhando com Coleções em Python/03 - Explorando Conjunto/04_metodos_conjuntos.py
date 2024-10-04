# union
## unir dois conjuntos em um único conjunto
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
print(conjunto1.union(conjunto2))

# intersection
## encontrar elementos comuns entre dois conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
print(conjunto1.intersection(conjunto2))

# difference
## encontrar elementos que estão em um conjunto e não no outro
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
print(conjunto1.difference(conjunto2))
print(conjunto2.difference(conjunto1))

# symmetric_difference
## encontrar elementos que estão em um conjunto ou no outro, mas não em ambos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
print(conjunto1.symmetric_difference(conjunto2))

# issubset
## verificar se um conjunto é um subconjunto de outro conjunto
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {1, 2, 3, 4, 5, 6, 7, 8}
print(conjunto1.issubset(conjunto2))
print(conjunto2.issubset(conjunto1))

# issuperset
## verificar se um conjunto é um superconjunto de outro conjunto
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {1, 2, 3, 4, 5, 6, 7, 8}
print(conjunto1.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto1))

# isdisjoint
## verificar se dois conjuntos são disjuntos (não têm elementos em comum)
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {6, 7, 8, 9, 10}
conjunto3 = {1, 4, 5, 6}
print(conjunto1.isdisjoint(conjunto2))
print(conjunto1.isdisjoint(conjunto3))

# add
## adicionar um elemento a um conjunto
conjunto = {1, 2, 3, 4, 5}
conjunto.add(6)
conjunto.add(5)
print(conjunto)

# clear
## remover todos os elementos de um conjunto
conjunto = {1, 2, 3, 4, 5}
print(conjunto)
conjunto.clear()
print(conjunto)

# copy
## criar uma cópia de um conjunto
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = conjunto1.copy()
print(conjunto2)

# discard
## remover um elemento de um conjunto se ele existir
conjunto = {1, 2, 3, 4, 5}
conjunto.discard(1)
print(conjunto)

# pop
## remover um elemento aleatório de um conjunto
conjunto = {1, 2, 3, 4, 5}
conjunto.pop()
print(conjunto)

# remove
## remover um elemento de um conjunto se ele existir
conjunto = {1, 2, 3, 4, 5}
conjunto.remove(2)
print(conjunto)

# len
## obter o número de elementos de um conjunto
conjunto = {1, 2, 3, 4, 5}
print(len(conjunto))

# in
## verificar se um elemento está em um conjunto
conjunto = {1, 2, 3, 4, 5}
print(3 in conjunto)
print(6 in conjunto)
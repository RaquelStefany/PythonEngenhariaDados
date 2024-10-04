# Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que tuplas são imutáveis enquanto listas são mutáveis.
# Isso significa que você não pode alterar os elementos de uma tupla, mas pode alterar os elementos de uma lista.

# Criando tupla colocando valores separados por virgulas de parenteses
frutas = ("laranja", "pera", "uva",)
print(frutas)

# Criando tupla usando classe tuple
letras = tuple(["python", "php"])
print(letras)

# Os métodos da tupla são basicamente os mesmos da lista
# O método index() retorna o índice do elemento especificado
print(letras.index("python"))
# O método count() retorna a quantidade de elementos especificados
print(letras.count("php"))
# O método len() retorna a quantidade de elementos da tupla
print(len(letras))

## Exceto:
# O método append() não existe na tupla, pois ela é imutável
# O método insert() não existe na tupla, pois ela é imutável
# O método remove() não existe na tupla, pois ela é imutável
# O método sort() não existe na tupla, pois ela é imutável
# O método reverse() não existe na tupla, pois ela é imutável
# O método pop() não existe na tupla, pois ela é imutável
# O método clear() não existe na tupla, pois ela é imutável
# O método copy() não existe na tupla, pois ela é imutável
# O método extend() não existe na tupla, pois ela é imutável
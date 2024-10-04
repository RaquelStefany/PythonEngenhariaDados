lista = []

# append
## Adicionar um valor a lista
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])
print(lista)

# clear
## Usado para limpar a lista
lista.clear()
print(lista)

# copy
## Usado para criar uma cópia da lista
lista = [1, "Python", [40, 30, 20]]
lista2 = lista.copy()
lista2[0] = 2
print(lista2)

# count
## Usado para contar a quantidade de um valor específico na lista
lista = [1, 2, 2, 3, 4, 4, 4]
print(lista.count(1), lista.count(2), lista.count(3), lista.count(4))

# extend
## Usado para adicionar vários valores a lista
linguagens = ["python", "php"]
print(linguagens)
linguagens.extend(["javascript", "sql"])
print(linguagens)

# index
## Usado para encontrar a posição de um valor específico na lista
linguagens = ["python", "php", "javascript", "sql"]
print(linguagens.index("php"))

# pop
## Usado para remover o último valor da lista
linguagens = ["python", "php", "javascript", "sql"]
linguagens.pop()
print(linguagens)
linguagens.pop(0)
print(linguagens)

# remove
## Usado para remover o primeiro valor da lista que for igual ao valor especificado
linguagens = ["python", "php", "javascript", "sql"]
linguagens.remove("javascript")
print(linguagens)

# reverse
## Usado para inverter a ordem da lista
linguagens = ["python", "php", "javascript", "sql"]
linguagens.reverse()
print(linguagens)

# sort
## Usado para ordenar a lista em ordem
linguagens = ["python", "php", "javascript", "sql"]
### Ordenar a lista em ordem crescente
linguagens.sort()
print(linguagens)
### Ordenar a lista em ordem decrescente
linguagens.sort(reverse=True)
print(linguagens)
### Ordenar a lista em tamanho crescente dos caracteres
linguagens.sort(key=len)
print(linguagens)
### Ordenar a lista em tamanho decrescente dos caracteres
linguagens.sort(key=len, reverse=True)
print(linguagens)

# len
## Usado para encontrar o tamanho da lista
linguagens = ["python", "php", "javascript", "sql"]
print(len(linguagens))

# sorted
## Usado para ordenar a lista em ordem sem alterar a lista original
linguagens = ["python", "php", "javascript", "sql"]
### Exibir a lista em ordem crescente
print(sorted(linguagens))
### Exibir a lista em ordem decrescente
print(sorted(linguagens, reverse=True))

print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0])
# Um dicionario é um conjunto não-ordenado de pares chave valor. 
# Em Python, os dicionarios são representados por chaves e são mutaveis.

# declarando um dicionario
# usando {}
pessoa = {
    "nome": "Raquel",
    "idade": 21,
}

# usando dist
pessoa = dict(
    nome="Raquel",
    idade=21,
)

# adicionando uma nova chave
pessoa["altura"] = 1.58

# acessando dicionario
print(pessoa)
print(pessoa["nome"])
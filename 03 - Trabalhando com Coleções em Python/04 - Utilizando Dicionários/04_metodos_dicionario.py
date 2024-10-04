contatos = {
    "raquel@email.com": {
        "nome": "Raquel",
        "telefone": "(11) 11111-1111",
    },
    "rayssa@email.com": {
        "nome": "Rayssa",
        "telefone": "(22) 22222-2222",
    },
    "regina@email.com": {
        "nome": "Regina",
        "telefone": "(33) 33333-3333",
    },
}

# clear
# usado para limpar o dicionario
contatos.clear()
print(contatos)

contatos = {
    "raquel@email.com": {
        "nome": "Raquel",
        "telefone": "(11) 11111-1111",
    }
}

# copy
# usado para criar uma cópia do dicionario
contatos_copia = contatos.copy()
print(contatos_copia)

# fromkeys()
# usado para criar um dicionario com as chaves especificadas e valores padrão
contatos = dict.fromkeys(
    ["rayssa@email.com", "regina@email.com"],
    {"nome": "Nome", "telefone": "Telefone"},
)
print(contatos)

# get()
# usado para buscar um valor no dicionario
# se a chave não existir, ele retorna o valor padrão
print(contatos.get("raquel@email.com", "Chave não encontrada"))

# items()
# usado para buscar todas as chaves e valores do dicionario
print(contatos.items())

# keys()
# usado para buscar todas as chaves do dicionario
print(contatos.keys())

# pop()
# usado para remover um item do dicionario
# se a chave não existir, ele retorna o valor padrão
print(contatos.pop("wellington@email.com", "Chave não encontrada"))

# popitem()
# usado para remover o último item do dicionario
print(contatos.popitem())

#  setdefault()
# usado para buscar um valor no dicionario
# se a chave não existir, ele adiciona a chave e valor especificados
print(
    contatos.setdefault(
        "raquel@email.com", {"nome": "Raquel", "telefone": "(11) 11111-1111"}
    )
)
print(contatos)

# update()
# usado para adicionar novos itens ao dicionario
contatos.update({"raquel@email.com": {"nome": "Raquel"}})
print(contatos)
contatos.update({"raquel@email.com": {"nome": "Raquel", "telefone": "(22) 22222-2222"}})
print(contatos)

# values()
# usado para buscar todos os valores do dicionario
print(contatos.values())

# in
# usado para verificar se uma chave existe no dicionario
print("raquel@email.com" in contatos)

# del
# usado para remover um item do dicionario
del contatos["raquel@email.com"]['telefone']
print(contatos)
del contatos["raquel@email.com"]
print(contatos)
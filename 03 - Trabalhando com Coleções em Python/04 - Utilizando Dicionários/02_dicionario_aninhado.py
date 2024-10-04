# Dicionarios podem armazenar qualquer tipo de objeto Python como valor, 
# desde que a chave para esse valor seja um objeto mutável como strings e números.

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

print(contatos)
print(contatos["raquel@email.com"])
print(contatos["raquel@email.com"]["nome"])
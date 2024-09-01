def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


# Sem argumento nomeado
salvar_carro("Chevrolet", "Onix", 2020, "ABC-1234")

# Com argumento nomeado
salvar_carro(marca="Chevrolet", modelo="Onix", ano=2020, placa="ABC-1234")

# Com dicionario (*args ou **kwargs)
# Args = Recebe um tupla (argumentos separados por virgula)
# Kwargs = Recebe um dicionario (argumentos chave e valor)
salvar_carro(
    **{"marca": "Chevrolet", "modelo": "Onix", "ano": 2020, "placa": "ABC-1234"}
)
print()

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join(
        [f"{chave.title()}: {valor}" for chave, valor in kwargs.items()]
    )
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    return mensagem


poema = exibir_poema(
    "Domingo, 01 de Agosto de 2024", "Verso 1", "Verso 2", "Verso 3", autor="Autor", titulo="Titulo"
)
print(poema)
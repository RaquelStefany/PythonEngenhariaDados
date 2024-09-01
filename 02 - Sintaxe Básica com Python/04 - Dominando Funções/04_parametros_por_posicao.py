# Position Only
# Parâmetros após o /, são obrigatórios terem argumentos
def criar_carro_1(modelo, ano, placa, /, marca, motor, combustivel):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}/{motor}/{combustivel}")
    
criar_carro_1("Onix", 2020, "ABC-1234", marca="Chevrolet", motor="1.0", combustivel="Flex")

# Keyword Only
# Parâmetros após o *, são obrigatórios terem argumentos
def criar_carro_2(*, modelo, ano, placa, marca, motor, combustivel):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}/{motor}/{combustivel}")
    
criar_carro_2(modelo="Onix", ano=2020, placa="ABC-1234", marca="Chevrolet", motor="1.0", combustivel="Flex")
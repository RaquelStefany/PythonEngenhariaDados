# A forma mais comum de percorrer os dados de um conjunto é utilizando o for

carros = {"gol", "celta", "palio", "gol"}
for carro in carros:
    print(carro)
    

# Quando é necessário saber o índice do objeto utilizamos enumerate
carros = {"gol", "celta", "palio", "gol"}
for indice, carro in enumerate(carros):
    print(f"O índice é {indice} e o carro é {carro}")
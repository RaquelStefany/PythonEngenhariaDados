# Função com retorno
def calcular_total(numeros):
    return sum(numeros)

print(calcular_total([1, 2, 3, 4, 5]))

# Função com retorno múltiplo
def calcular_total_e_media(numeros):
    total = sum(numeros)
    media = total / len(numeros)
    return total, media

print(calcular_total_e_media([1, 2, 3, 4, 5]))

# Função sem retorno explicito
def imprimir_mensagem(mensagem):
    print(mensagem)
    
print(imprimir_mensagem('Olá, mundo!'))
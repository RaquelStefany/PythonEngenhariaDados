# A palavra-chave global informa ao interpretador que a variável que está sendo manipulada no escopo local é global.
## Essa NÃO é uma boa prática e deve ser evitada.

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))
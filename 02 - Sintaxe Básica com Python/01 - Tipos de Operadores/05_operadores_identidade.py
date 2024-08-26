# São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

# Operador "is"
print(curso is nome_curso)
print(saldo is limite)

# Operador "is not"
print(curso is not nome_curso)
print(saldo is not limite)
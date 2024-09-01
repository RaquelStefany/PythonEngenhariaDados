# Função é um bloco de código identificado por um nome epode receber uma lista de parâmetros, esses parâmetros podem ou não ter valores padrões.

# Função sem parâmetros
def funcao_sem_parametros():
    print('Olá Mundo!')
    
funcao_sem_parametros()

# Função com parâmetros
def funcao_com_parametros(nome):
    print('Olá', nome)
    
funcao_com_parametros('Fulano')

# Função com parâmetros e valor padrão
def funcao_com_parametros_padrao(nome='Mundo'):
    print('Olá', nome)
    
funcao_com_parametros_padrao()
funcao_com_parametros_padrao('Fulano')
nome = "Raquel"
idade = 21
profissao = "Analista de Sistemas"
linguagem = "Python"

# Old style %
print("Olá, me chamo %s. Tenho %d anos de idade.\nTrabalho como %s e estou matriculada no curso de %s." % (nome, idade, profissao, linguagem))

# New style .format()
print("Olá, me chamo {}. Tenho {} anos de idade.\nTrabalho como {} e estou matriculada no curso de {}.".format(nome, idade, profissao, linguagem))

# f-string
print(f"Olá, me chamo {nome}. Tenho {idade} anos de idade.\nTrabalho como {profissao} e estou matriculada no curso de {linguagem}.")
from datetime import datetime, timedelta

# pegando data
data = datetime.now()
print(data)

# adicionando cinco minutos
data += timedelta(minutes=5)
print(data)

# adicionando uma hora
data += timedelta(hours=1)
print(data)

# adicionando um dia
data += timedelta(days=1)
print(data)

# adicionando uma semana
data += timedelta(weeks=1)
print(data)

# adicionando um mês
data += timedelta(days=30)
print(data)
from datetime import date, datetime, time

# data manual
dataManual = date(2024, 10, 4)
print(dataManual)

# data atual
dataAtual = date.today()
print(dataAtual)

# data e hora manual
dataHoraManual = datetime(2024, 10, 4, 10, 30, 15)
print(dataHoraManual)

# data e hora atual
dataHoraAtual = datetime.now()
print(dataHoraAtual)

# hora manual
horaManual = time(10, 30, 15)
print(horaManual)
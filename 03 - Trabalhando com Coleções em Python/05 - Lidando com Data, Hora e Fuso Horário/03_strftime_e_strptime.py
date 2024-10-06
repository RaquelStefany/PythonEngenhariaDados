from datetime import datetime

dataAtual = datetime.now()

# formatar data para DD/MM/AAAA HH:MM:SS
dataFormatada = dataAtual.strftime('%d/%m/%Y %H:%M:%S')
print(dataFormatada)

# convertendo string para data
dataString = "2022-01-01 00:00:00"
dataFormatada = datetime.strptime(dataString, '%Y-%m-%d %H:%M:%S')
print(dataFormatada)

# pegar dia da semana
dataFormatada = datetime.strptime(dataString, '%Y-%m-%d %H:%M:%S')
print(dataFormatada.strftime('%A'))  # exibe o dia da semana
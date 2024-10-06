from datetime import datetime
import pytz

# criando data com timezone São Paulo
data = datetime.now(pytz.timezone('America/Sao_Paulo'))
print("Data São Paulo:", data)

# criando data com timezone Oslo
data = datetime.now(pytz.timezone('Europe/Oslo'))
print("Data Oslo:", data)

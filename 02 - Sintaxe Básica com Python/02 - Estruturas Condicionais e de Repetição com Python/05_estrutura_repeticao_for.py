texto = input("Informe um texto: ")
vogais = "AEIOU"

# for com if
for letra in texto:
    if letra.upper() in vogais:
        print(letra)
        
# for com built-in range
for i in range(len(texto)):
    if texto[i].upper() in vogais:
        print(texto[i])

for numero in range(0, 11):
    print(numero)
    
for numero in range(0, 51, 5):
    print(numero)

for numero in range(100):
    if numero == 77:
        break
    print(numero)
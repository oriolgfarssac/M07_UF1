frase = input("Introdueix una frase: ")

fraseSenseEspais = frase.replace(" ", "")

fraseSenseRepetits = fraseSenseEspais[0]

allargada = len(fraseSenseEspais)

for char in fraseSenseEspais:
    if char not in fraseSenseRepetits:
        fraseSenseRepetits += char


paraules = tuple(fraseSenseEspais)

print(paraules)
print(fraseSenseRepetits)

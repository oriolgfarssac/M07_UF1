numeros = input("Introdueix 10 numeros separats per espais")

numeros = numeros.split()

llistaNumeros = []

sumaNumeros = 0

for numero in numeros:
    llistaNumeros.append(numero)

for numero in llistaNumeros:
    sumaNumeros = sumaNumeros + int(numero)

mitjanaNumeros = sumaNumeros/10

llistaNumeros.append(sumaNumeros)
llistaNumeros.append(mitjanaNumeros)

print("Numeros de l'usuari: ", llistaNumeros[0:10])
print("Suma dels numeros: ", (llistaNumeros[10]))
print("Mitjana dels numeros: ", llistaNumeros[11])

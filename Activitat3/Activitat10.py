abecedari = list('abcdefghijklmnopqrstuvwxyz')

llista_filtrada = []

for i in range(len(abecedari)):
    if i % 3 != 0 or i == 0:
        llista_filtrada.append(abecedari[i])

tupla_resultant = tuple(llista_filtrada)

print("Llista resultant:", llista_filtrada)
print("Tupla resultant:", tupla_resultant)

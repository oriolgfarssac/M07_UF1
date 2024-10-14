from exercici1 import exercici1
from exercici4_Arman import matriuRandom
from exercici4_Arman import segonaMatriu
from exercici4_Arman import terceraMatriu

matriu = exercici1()

print("Exercici 1 del Arman", "\n" )
print("Del exercici 1 la matriu", "\n" , matriu, "\n")

dimensioMatriu = matriu.ndim
print(f"Del exercici 1 la dimensió de la matriu: {dimensioMatriu}", "\n")

tamanyMatriu = matriu.shape
print(f"Del exercici 1 el tamany de la matriu: {tamanyMatriu}", "\n")

totalElements = matriu.size
print(f"Del exercici 1 el Número total d’elements: {totalElements}", "\n")

tipusElements = matriu.dtype
print(f"Del exercici 1 el Tipus d’elements interns: {tipusElements}", "\n")


print("Exercici 4 del Arman", "\n" )
matriuRandom = matriuRandom()
print(f"Exercici 4 Arman Matriu de 3x4 de números aleatoris de 0 a 80: \n", matriuRandom, "\n")


matriu2 = segonaMatriu(matriuRandom)
print(f"Exercici 4 Arman la última columna passa a ser la última fila: \n", matriu2, "\n")


matriu3 = terceraMatriu(matriu2)
print(f"Exercici 4 Arman La nova matriu haurà de tindre els mateixos números en la última columna (han de ser iguals al primer número de la última columna de la matriu anterior): \n", matriu3, "\n")

